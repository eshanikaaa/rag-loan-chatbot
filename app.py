import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI  # or use another LLM if available

# Load FAISS vectorstore
vectorstore = FAISS.load_local(
    "vectorstore",
    HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"),
    allow_dangerous_deserialization=True
)

# Setup retriever
retriever = vectorstore.as_retriever()

# Use a language model (requires OpenAI API key set in environment or .env)
llm = OpenAI(temperature=0.7)

# RAG Chain
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# Streamlit UI
st.title("📄 Loan Approval RAG Chatbot")
query = st.text_input("Ask a question about loan approvals")

if query:
    answer = qa_chain.run(query)
    st.write("Answer:", answer)
