import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_classic.chains import create_history_aware_retriever
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from .data_loader import load_and_split_data

# --- GLOBAL SETUP ---
load_dotenv()

# Verify key exists
if not os.environ.get("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found. Please check your .env file.")

# 2. Prepare Vector Store
splits = load_and_split_data()
vectorstore = FAISS.from_documents(
    documents=splits, embedding=OpenAIEmbeddings())
retriever = vectorstore.as_retriever()

# 3. Setup LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# --- 1. THE REPHRASER (Grammar Fixer) ---
contextualize_q_system_prompt = """Given a chat history and the latest user question 
which might reference context in the chat history, formulate a standalone question 
which can be understood without the chat history.

CRITICAL RULES:
1. If the user asks "Is he know [X]?" or "Does he know [X]?", rewrite it as: "Is [X] listed in Chamod's Skills or Projects?"
2. Fix broken grammar (e.g., "is he know" -> "Does he know").
3. Do NOT answer the question, just rewrite it."""

contextualize_q_prompt = ChatPromptTemplate.from_messages([
    ("system", contextualize_q_system_prompt),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}"),
])

# --- 2. THE FRIENDLY PERSONA (Chamzz) ---
qa_system_prompt = """You are "Chamzz" (Chamod's AI Bot) 🤖. 
You are super friendly, enthusiastic, and helpful! 🌟

RULES FOR ANSWERING:
1. **Skill Proficiency:** - If the user asks "How good is he at [Skill]?" or "Rate his [Skill]", check the 'SKILL PROFICIENCY' section.
   - If it's **Expert**: "He's an Expert at that! 🏆 It's part of his core stack and he uses it mainly for [Context from Projects]."
   - If it's **Proficient**: "He is very proficient! 🛠️ He uses it daily in his projects."
   - If it's **Familiar**: "He has experience with it! 📚 He's used it in past projects like [Project Name]."
   
2. **Current Learning:**
   - If asked "What is he learning?" or "What's new?", refer to the 'CURRENTLY LEARNING' section. Be excited about it! (e.g., "He's currently diving deep into Rust! 🦀")

3. **General Projects/Education:** Use emojis and bullet points.

4. **Contact:** If unsure, say: "I'm not sure! 🤔 Try emailing him at chamodsugathadasa@gmail.com 📩"

Context: {context}"""

qa_prompt = ChatPromptTemplate.from_messages([
    ("system", qa_system_prompt),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}"),
])

# 5. Build Chains
history_aware_retriever = create_history_aware_retriever(
    llm, retriever, contextualize_q_prompt)
question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)
rag_chain = create_retrieval_chain(
    history_aware_retriever, question_answer_chain)

# 6. Memory Management
store = {}


def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


conversational_rag_chain = RunnableWithMessageHistory(
    rag_chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="answer",
)


def generate_response(message, thread_id):
    response = conversational_rag_chain.invoke(
        {"input": message},
        config={"configurable": {"session_id": thread_id}}
    )
    return response["answer"]
