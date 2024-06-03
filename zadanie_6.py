import streamlit as st

def sum2(a,b):
    return int(a) + int(b)

st.title("Kalkulator")

first_number = st.text_input("Podaj pierwsza liczbe")
second_number = st.text_input("Podaj druga liczbe ")

button = st.button("send")


if button:
    with st.spinner("Generuje odpowiedz ..."):
        suma = sum2(first_number, second_number)
        st.write(suma)

