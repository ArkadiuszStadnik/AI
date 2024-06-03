import os
import chromadb
import requests
from bs4 import BeautifulSoup
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import CharacterTextSplitter


SRC_DIR = os.path.dirname(os.path.abspath(__file__))
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
def insert_pdf_to_chromadb():
    pdf_folder_path = SRC_DIR + "/istqb-documents"
    documents = []
    for file in os.listdir(pdf_folder_path):
        print(file.title())
        if file.endswith('.pdf'):
            pdf_path = os.path.join(pdf_folder_path, file)
            loader = PyPDFLoader(pdf_path)
            documents.extend(loader.load())
    text_splitter = CharacterTextSplitter(chunk_size=400, chunk_overlap=0)
    chunked_documents = text_splitter.split_documents(documents)
    client = chromadb.Client()
    vectordb = Chroma.from_documents(
        documents=chunked_documents,
        embedding=embeddings,
        collection_name="my_first_collection",
        persist_directory=SRC_DIR + "/chroma-testowo"
    )


def insert_text_url_to_chromadb(url):
    text_scrap_array = []
    response = requests.get(url).text
    soap = BeautifulSoup(response, 'html.parser')
    wynik_p = soap.find_all("p")
    for paragraph in wynik_p:
        text_scrap_array.append(paragraph.text)
    text_scrap = " ".join(text_scrap_array)
    text_splitter = CharacterTextSplitter(chunk_size=400, chunk_overlap=0)
    texts = text_splitter.create_documents([text_scrap])
    chunked_documents = text_splitter.split_documents(texts)
    client = chromadb.Client()
    vectordb = Chroma.from_documents(
        documents=chunked_documents,
        embedding=embeddings,
        collection_name="my_first_collection",
        persist_directory=SRC_DIR + "/chroma-testowo"
    )

insert_text_url_to_chromadb("https://pl.wikipedia.org/wiki/Mariusz_Pudzianowski")