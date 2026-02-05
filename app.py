import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv
from langchain_logic.rag import generate_response

# Load environment variables
load_dotenv()

app = Flask(__name__)

# --- 1. SECURITY CONFIGURATION ---

# Define allowed domains
ALLOWED_DOMAINS = ["*"]


# Enable CORS (Browser Protection)
CORS(app, resources={
     r"/chat": {"origins": ALLOWED_DOMAINS}})

# Setup Rate Limiter (Spam Protection)
# This limits users by their IP address
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://"
)

# --- 2. THE CHAT ENDPOINT ---


@app.route('/chat', methods=['POST'])
@limiter.limit("5 per minute")  # <--- Rule: Max 5 messages per minute per IP
def chat():
    # --- LEVEL 1: Strict Origin Check ---
    # Browsers send 'Origin' automatically. Postman does NOT unless manually added.
    origin = request.headers.get('Origin')

    # Allow if it's your site OR localhost (for testing)
    # if origin not in ALLOWED_DOMAINS:
    #     return jsonify({"error": "Access Denied: Invalid Origin"}), 403

    # --- LEVEL 2: Secret Key Check ---
    # You must send this header from your Frontend
    secret_key = request.headers.get('X-Portfolio-Key')
    if secret_key != os.environ.get("MY_PORTFOLIO_SECRET"):
        return jsonify({"error": "Unauthorized: Invalid Key"}), 401

    # --- LEVEL 3: Standard Logic ---
    data = request.json
    user_message = data.get('message')
    thread_id = data.get('thread_id')

    if not user_message or not thread_id:
        return jsonify({"error": "Missing data"}), 400

    try:
        bot_reply = generate_response(user_message, thread_id)
        print({"user_message": user_message,
               "thread_id": thread_id,
               "reply": bot_reply})

        return jsonify({"reply": bot_reply})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Internal Server Error"}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
