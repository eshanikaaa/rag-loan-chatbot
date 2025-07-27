# 🧠 RAG Loan Chatbot

A Retrieval-Augmented Generation (RAG) based chatbot that intelligently answers queries related to loan approval using a dataset and document retrieval. This project combines traditional vector search with generative AI to build a powerful and contextual chatbot interface using Streamlit.

---

## Features

-  Chatbot interface using Streamlit
-  Retrieval-Augmented Generation using LangChain
-  FAISS-based vector store for document retrieval
-  Document chunking and embedding with HuggingFace Transformers
-  Custom preprocessing pipeline for text cleaning
-  Uses Loan Approval dataset from Kaggle for knowledge grounding

---

## 🗂️ Project Structure
rag_loan_chatbot/
│
├── app.py # Streamlit frontend
├── build_vectorstore.py # Builds FAISS vectorstore from dataset
├── load_data.py # Loads and parses CSV files
├── preprocess.py # Text preprocessing utilities
├── Training Dataset.csv # Source dataset
├── faiss_index/ # Stores FAISS .faiss and .pkl index files
│ └── index.faiss
│ └── index.pkl
├── chatbot_reqs.txt # Requirements file for chatbot dependencies
└── test_load_preprocess.py # Test script for load and preprocess

How It Works
Preprocessing: Cleans and prepares the loan-related data.
Vectorization: Chunks and embeds the dataset using HuggingFace embeddings.
Retrieval: FAISS retrieves relevant chunks for user queries.
Generation: LangChain + OpenAI/Gemini generates answers grounded in retrieved chunks.

 Dataset
Loan Prediction Dataset – Kaggle
