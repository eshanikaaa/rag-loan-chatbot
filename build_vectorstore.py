import os
import pandas as pd
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document
from load_data import load_dataset
from preprocess import preprocess_data

def build_vectorstore(csv_path, faiss_index_path):
    df = load_dataset(csv_path)
    processed_data = preprocess_data(df)

    docs = [Document(page_content=row) for row in processed_data]

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = FAISS.from_documents(docs, embeddings)

    db.save_local(faiss_index_path)
    print(f"✅ FAISS vectorstore saved at: {faiss_index_path}")

if __name__ == "__main__":
    build_vectorstore("Training Dataset.csv", "faiss_index")
