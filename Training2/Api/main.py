import os

import chromadb
from fastapi import FastAPI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms.ctransformers import CTransformers
from langchain_community.vectorstores import Chroma


app = FastAPI()

llm = CTransformers(model="/home/student/PycharmProjects/AIProject/llama-2-7b-chat.Q4_K_M.gguf", model_type="llama")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/promprt/{item_id}/{collection}")
def get_answer(item_id: str, collection: str):
    wynik = llm.invoke("[INST]" + "Odpowiedz na pytanie w języku polskim: " + item_id + "w oparciu o tekst. Tekst: "
                       + preapreCollectionAndReturnChunk(collection,item_id) + "[/INST]")
    return {"response": wynik}


@app.get("/promprt/{item_id}/")
def get_answer(item_id: str):
    wynik = llm.invoke("[INST]" + item_id+"[/INST]")
    return {"response": wynik}

def preapreCollectionAndReturnChunk(collection,pytanie):
    client = chromadb.PersistentClient(path= "/home/student/PycharmProjects/AIProject/Training2/chroma-testowo")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    client.get_collection(collection)
    langchain_chroma = Chroma(persist_directory="/home/student/PycharmProjects/AIProject/Training2/chroma-testowo",
                         collection_name=collection,
                         embedding_function=embeddings)
    text = langchain_chroma.as_retriever().invoke(pytanie)
    return text[0].page_content