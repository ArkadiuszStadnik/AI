import os

import chromadb
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma



def get_chunk_from_vectordb(chromafolder,pytanie):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    langchain_chroma = Chroma(persist_directory=chromafolder,
                         collection_name="my_first_collection",
                         embedding_function=embeddings)
    text = langchain_chroma.as_retriever().invoke(pytanie)
    return text[1].page_content
