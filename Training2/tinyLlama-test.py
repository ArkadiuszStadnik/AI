import os

from Training2.chromadb_connector.chromadb_connector import get_chunk_from_vectordb
from llama.connector import ask_ollama, ask_ollama_for_rag

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
path=SRC_DIR + "/chroma-testowo"

text = get_chunk_from_vectordb(path,"What is testing")

print("********************TINYLLAMA WITH RAG********************")
print(ask_ollama_for_rag("What you know about testing",text))

print("********************CHROMA********************")
print(get_chunk_from_vectordb(path,"What you know about testing"))


print("********************TINYLLAMA********************")
print(ask_ollama("What you know about testing"))








