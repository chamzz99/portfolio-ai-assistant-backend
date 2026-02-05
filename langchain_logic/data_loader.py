from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


CV_TEXT = """
Name: Chamod Sugathadasa
Role: Software Engineer - AI Full Stack
Email: chamodsugathadasa@gmail.com
Links: chamo.is-a.dev, LinkedIn/chamod-sugathadasa, GitHub/chamzz99

--- SUMMARY ---
Software Engineer passionate about building AI powered applications. I combine frontend development, backend systems, and AI technologies.

--- CURRENTLY LEARNING & GOALS ---
I am a lifelong learner! Right now, I am focusing on:
1. Generative AI: Studying Agentic LangChain and LangGraph to build smarter AI systems.
2. AI Image Generation: Studying image synthesis and diffusion models to create visual AI content.
3. Go: Exploring Go for high-performance systems programming.
4. Cloud Architecture: Deepening my knowledge of AWS Solution Architecture.

--- SKILL PROFICIENCY ---
* **Expert (My Core Stack):** Python, FastAPI, Flask, SQL, RAG (Retrieval Augmented Generation).
* **Proficient (Use Daily):** React.js, JavaScript, YOLO, OpenCV, LangChain, OpenAI API, MongoDB, Google Cloud Platform (GCP), HTML/CSS.
* **Familiar (Experience with):** Java, PHP, TypeScript, Laravel, Angular, AWS, Docker, Airflow.

--- RESEARCH ---
"Design and Development of a Reusable Chatbot for Fashion Recommendations: Sinhala Language as a Case Study" (ICBI 2024).
- **Publication Link:** [https://www.researchgate.net/publication/395464824_Design_and_Development_of_a_Reusable_Chatbot_for_Fashion_Recommendations_Sinhala_Language_as_a_Case_Study]
- **Technologies:** Python, Flask, OpenAI API, Bing Translator API.
- **Innovation:** Designed a cross-lingual chatbot using Soft Design Science Research Methodology (SDSRM). It uses a bi-directional translation middleware to allow Sinhala speakers to interact with GPT models.
- **Deployed Link:** [https://chamzz.pythonanywhere.com]

--- DETAILED PROJECT LIST (ALL PROJECTS) ---

1. [Data Engineering & Full Stack] ATM Cash Load Prediction System (Evoq Systems)
   - Technologies: Python, NumPy, Pandas, React, FastAPI, MongoDB, Airflow, Docker.
   - Database: Used MongoDB to store machine-learning predictions.
   - Full Stack: Built a React/D3.js dashboard with a FastAPI backend.
   - Engineering: Created an automated ETL pipeline using Python/Regex to clean ATM logs.

2. [AI & Backend] AI Travel Itinerary Generator (Evoq Systems)
   - Technologies: Python, Flask, Google Gemini, GCP, Python-Docx.
   - Styled Document Generation: Engineered a parsing engine using 'python-docx' to generate professionally styled, downloadable Word itineraries from JSON data.
   - Backend: Architected the complete backend using Flask and RESTful APIs.

3. [Computer Vision] Real-Time Object Counting System (Evoq Systems)
   - Technologies: Python, TensorFlow, YOLO, OpenCV, PyQt, MongoDB.
   - Desktop GUI: Built a real-time desktop interface using PyQt.
   - Data Persistence: Integrated MongoDB to store counting data and Loguru for error tracking.
   - AI: Trained a custom YOLO model with 99% accuracy.

4. [Computer Vision] Automated Garment Defect Detection System (Evoq Systems)
   - Technologies: Python, YOLO, PyQt, OpenCV, Excel Automation, MongoDB.
   - Desktop GUI: Designed a PyQt dashboard for real-time monitoring of defects.
   - Database: Automatically aggregates inspection data from MongoDB to generate Excel reports.
   - Algorithm: Combined YOLO and OpenCV Edge Detection to replace manual inspections.

5. [GenAI & Frontend] ILO (Intended Learning Outcome) Analyzer (Thesara)
   - Technologies: Python, Flask, OpenAI API, HTML/CSS.
   - Details: Implemented RAG architecture to validate educational rules against Bloom's Taxonomy.

6. [Full Stack] User Management System (Thesara)
   - Technologies: Angular, TypeScript, PHP, Laravel, SASS.
   - Frontend: Designed a fully responsive, modular UI using Angular and SASS.
   - Backend: Engineered scalable server-side logic using Laravel.

7. [Infrastructure] Moodle LMS Deployment (Thesara)
   - Technologies: Moodle, Linux, MySQL.
   - Details: Configured and deployed Moodle LMS for educational institutes.

--- EDUCATION ---
Bachelor of Commerce (Special) Degree in Business Technology
- Institute: University of Kelaniya, Sri Lanka (3.57 GPA).

--- PERSONAL INTERESTS ---
- Gaming 🎮, Cricket 🏏, Movies 🎬, Travelling ✈️.
"""


def load_and_split_data():
    docs = [Document(page_content=CV_TEXT)]
    # Chunk size 1500 ensures Research stays connected to its Link and Description
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    return splits
