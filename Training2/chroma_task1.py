import os
import streamlit as st
import chromadb
import requests
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
client = chromadb.PersistentClient(path=SRC_DIR + "/chroma-testowo")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")




def ask_llama3(pytanie, tekst):
    url = 'http://localhost:11434/api/generate'
    data = {
        "model": "llama3",
        "prompt": "Odpowiedz na pytanie: " + pytanie + "w oparciu tekst. Tekst: " + tekst,
        "stream": False
    }

    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Sukces!")
        print("Odpowiedź serwera:")
        print(response.json()["response"])
    else:
        print("Błąd! Kod statusu:", response.status_code)
    return response.json()["response"]

def preapreCollectionAndReturnChunk():
    collection = client.get_collection("my_first_collection")
    langchain_chroma = Chroma(persist_directory=SRC_DIR + "/chroma-testowo",
                         collection_name="my_first_collection",
                         embedding_function=embeddings)
    text = langchain_chroma.as_retriever().invoke(pytanie)
    return text[0].page_content

def preapreCollectionAndReturnChunk(collection):
    client.get_collection(collection)
    langchain_chroma = Chroma(persist_directory=SRC_DIR + "/chroma-testowo",
                         collection_name=collection,
                         embedding_function=embeddings)
    text = langchain_chroma.as_retriever().invoke(pytanie)
    return text[0].page_content


def ask_llama3(pytanie):
    url = 'http://localhost:11434/api/generate'
    data = {
        "model": "llama3",
        "prompt": "Odpowiedz na pytanie w języku polskim: " + pytanie + "w oparciu o tekst. Tekst: " + preapreCollectionAndReturnChunk(),
        "stream": False
    }

    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Sukces!")
        print("Odpowiedź serwera:")
        print(response.json()["response"])
    else:
        print("Błąd! Kod statusu:", response.status_code)
    return response.json()["response"]



#Streamlit UI
pytanie = st.text_input("Pytanie")


if st.button("Send question"):
    with st.spinner("Pobieranie danych..."):
        st.write(ask_llama3(pytanie))