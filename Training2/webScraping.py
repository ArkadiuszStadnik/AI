import requests
import streamlit as st
from bs4 import BeautifulSoup


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


url = st.text_input("Podaj adres URL")



pytanie = st.text_input("Pytanie")



if st.button("Pobierz stronę"):
    response = requests.get(url).text
    soap = BeautifulSoup(response, 'html.parser')
    wynik_p = soap.find_all("p")
    with st.spinner("Pobieranie danych..."):
        st.write(ask_llama3(pytanie, str(wynik_p)))