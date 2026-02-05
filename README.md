# 🤖 AI Portfolio AI Assistant (Backend)

> **Turn your static Resume into an intelligent, conversational AI Assistant.**

This repository contains the backend code for a **RAG-powered (Retrieval Augmented Generation)** Chatbot designed for personal portfolios. It allows visitors to chat with an AI version of you, asking questions about your experience, skills, and projects in a natural, conversational way.

Built with **Flask**, **LangChain**, and **OpenAI**, this assistant features short-term memory, context rephrasing, and a customizable persona.

---

## 🚀 Features & Technologies

### Key Features

- **🧠 RAG Architecture:** Answers questions strictly based on _your_ specific data (CV/Resume), minimizing hallucinations.
- **💬 Conversational Memory:** Remembers context (e.g., "What is **his** email?" understands "he" refers to the profile owner).
- **🔄 Smart Rephrasing:** Automatically fixes broken grammar and resolves pronouns before searching the database.
- **🎭 Custom Persona:** Easily adjustable tone (Friendly/Professional) and personality (currently set to "Chamzz" - a friendly tech enthusiast).
- **🔌 API-First:** Built as a REST API (Flask) to easily integrate with React, Vue, or any frontend portfolio.

### Tech Stack

- **Python 3.10+**
- **Flask** (Web Server)
- **LangChain** (LLM Orchestration & Chains)
- **FAISS** (Vector Store for efficient retrieval)
- **OpenAI GPT-4o-mini** (Cost-effective, high-intelligence Model)
- **Python-Dotenv** (Security)

---

## 📂 Project Structure & File Guide

Here is the file structure of the backend. The most important file for customization is `data_loader.py`.

```text
portfolio-ai-assistant-backend/
├── 📄 app.py                  # [ENTRY POINT] The Flask API server. Handles incoming HTTP requests.
├── 📄 requirements.txt        # [DEPENDENCIES] List of Python libraries needed to run the app.
├── 📄 .env                    # [SECURITY] Stores your OpenAI API Key.
└── 📁 langchain_logic/        # [THE BRAIN] Contains all AI logic.
    ├── 📄 __init__.py         # Makes this folder a Python package.
    ├── 📄 rag.py              # [LOGIC] Sets up the LLM, Prompts, Memory, and RAG Chain.
    └── 📄 data_loader.py      # [DATA] <-- EDIT THIS. Contains your CV_TEXT. Paste your raw resume/skills here.

```

---

## 📝 Detailed File Explanation

--**app.py:** The bridge between the web and the AI. It accepts JSON requests ({ "message": "...", "thread_id": "..." }) and sends back the AI's response.

--**langchain_logic/data_loader.py:** <-- EDIT THIS. This file contains the CV_TEXT variable. This is where you paste your raw resume text, projects, and skills. It handles splitting the text into chunks for the AI to read.

--**langchain_logic/rag.py:** The core intelligence. It initializes the OpenAI model, defines the system prompts (the "Persona"), and sets up the conversation history.

---

## ⚙️ How It Works (Architecture)

The assistant uses a RAG pipeline to retrieve relevant information from your resume before answering.

![AI Portfolio Architecture Diagram](/img/architecture-diagram.png)

1.  **User asks a question** via the API.
2.  **Memory Check:** The system looks up previous messages using the `thread_id`.
3.  **Rephrasing:** If the user says "Does _he_ know React?", the AI rewrites it to "Does _[Your Name]_ know React?" to ensure a good search.
4.  **Retrieval:** The system searches your `data_loader.py` content for the most relevant answers.
5.  **Generation:** The LLM constructs a friendly answer based _only_ on the facts found in your data.

---

## 🛠️ How to Run Locally

Follow these steps to get the bot running on your machine.

1. Clone the Repository
   ```text
   git clone [https://github.com/yourusername/portfolio-agent-backend.git](https://github.com/yourusername/portfolio-agent-backend.git)
   cd portfolio-agent-backend
   ```
2. Create a Virtual Environment

   # Windows

   ```text
   python -m venv venv
   venv\Scripts\activate
   ```

   # Mac/Linux

   ```text
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install Dependencies

   ```text
   pip install -r requirements.txt
   ```

4. Configure API Key

   Create a .env (Follow .env sample) file in the root directory and add your OpenAI API Key:

   ```text
   OPENAI_API_KEY=xx-xxx-xxxxxxxxxxxxxxxxxxxxxxxx
   ```

5. Customize Your Data

   Open langchain_logic/data_loader.py and replace the CV_TEXT content with your own Resume/Portfolio details.

6. Run the Server

   ```text
   python app.py
   ```

   The server will start at http://127.0.0.1:5000

---

## 🧪 Testing the API

You can test the bot using cURL or Postman.

Request:

    ```text
    curl -X POST [http://127.0.0.1:5000/chat](http://127.0.0.1:5000/chat) \
    -H "Content-Type: application/json" \
    -d '{"message": "What projects has he worked on?", "thread_id": "test_user_1"}'
    ```

Response:

    ```text
    JSON
    {
    "reply": "Chamod has worked on several exciting projects! 🚀 He built an Fashion recommendation Chatbot using OpenAI and Python..."
    }
    ```

---

## ☁️ Deployment

This project is ready to be deployed on PythonAnywhere, Heroku, or Render.

PythonAnywhere: Upload files, set up a virtualenv, and point the WSGI configuration file to wsgi.py.

Environment: Ensure you set the OPENAI_API_KEY in the production environment variables.

🤝 Contributing
Feel free to fork this repository and submit Pull Requests. If you find this template useful for your own portfolio, a star ⭐️ is appreciated!

Author: Chamod Sugathadasa
