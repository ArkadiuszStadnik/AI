import streamlit as st
import openai


def chatbot(pytanie):
    odpowiedz = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "Jesteś asyststentem testera oprogramowania"
            },
            {
                "role": "user",
                "content": pytanie
            }
        ],
        temperature=1,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        api_key="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"
    )

    return odpowiedz["choices"][0]["message"]["content"]


st.title("To jest moja pierwsza aplikacja web")

x = st.text_area("Podaj kod do review: ")

przycisk = st.button("sprwadz")

if przycisk:
    with st.spinner("Generuje odpowiedz ..."):
        odpowiedz = chatbot(x)
        st.write(odpowiedz)
