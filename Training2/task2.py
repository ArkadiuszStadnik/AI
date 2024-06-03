import streamlit as st
from PIL import Image
from langchain_community.llms.ctransformers import CTransformers

image = Image.open('/home/student/PycharmProjects/AIProject/monitor.jpg')
llm = CTransformers(model="/home/student/PycharmProjects/AIProject/llama-2-7b-chat.Q4_K_M.gguf", model_type="llama")


st.header('ChatBot Rlzzzzz')
st.header('_Streamlit_ is :blue[cool] :sunglasses:', divider='rainbow')

col1, col2 = st.columns(2)

with col1:
    st.header("Questions")
    question = st.text_input("Write the question")

with col2:
    st.image(image, caption='Monitor', use_column_width=True)
    st.header("Answers")
    if st.button("Get answer"):
        with st.spinner("Thinking..."):
            st.write(llm.invoke("[INST]" + "Ile to jest  "+question+"[/INST]"))