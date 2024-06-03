import streamlit as st
from langchain_community.llms.ctransformers import CTransformers

from main import print_hi


def chat_with_model(prompt ,model):
    print_hi('PyCharm')
    config = {'max_new_tokens': 300, 'repetition_penalty': 1.1, 'temperature': 0.2, 'top_k': 40, 'batch_size': 3,
              'top_p': 0.95}
    llm = CTransformers(model=f'{model}', model_type='llama', config=config)
    return (llm(f'''
    [INST]<<SYS>>
You are professional Python Developer
<</SYS>>[/INST]
[INST]
{prompt}
[/INST]
 '''))


st.title("Application with models")

prompt = st.text_input("Please provide prompt")
model = st.selectbox("Please Select model",(
             "codellama-7b-instruct.Q4_K_M.gguf",
             "llama-2-7b-chat.Q4_K_M.gguf",
             "llama-2-7b-chat.Q4_K_S.gguf"))

button = st.button("Send")

if button:
    with st.spinner('Wait for it...'):
        st.write(chat_with_model(prompt,model))
        st.success('Done!')
