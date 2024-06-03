import streamlit as st
from langchain_community.llms.ctransformers import CTransformers

llm = CTransformers(model="/home/student/PycharmProjects/AIProject/llama-2-7b-chat.Q4_K_M.gguf", model_type="llama")

a = st.text_input("A")
b = st.text_input("B")

operacja = st.selectbox("Operacja", ["+", "-", "*", "/"])

if st.button("Oblicz"):
    with st.spinner("Thinking..."):
        st.write(llm.invoke("[INST]"+a+" "+operacja+" "+b+"[/INST]"))