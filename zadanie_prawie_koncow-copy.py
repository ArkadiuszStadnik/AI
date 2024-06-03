import streamlit as st
from langchain_community.llms.ctransformers import CTransformers

from main import print_hi

from vectordb import Memory

from cw_9_dane import text2, text



def query(prompt):
    memory = Memory(chunking_strategy={'mode': 'sliding_window', 'window_size': 128, 'overlap': 16})
    metadata = {"title": "Introduction to Machine Learning",
                "url": "https://example.com/introduction-to-machine-learning"}
    memory.save(text, metadata)
    metadata2 = {"title": "Introduction to Artificial Intelligence",
                 "url": "https://example.com/introduction-to-artificial-intelligence"}
    memory.save(text2, metadata2)
    query = prompt
    results = memory.search(query, top_n=3)
    return results[0]['chunk']



def chat_with_model(prompt ,model):
    chunk = query(prompt)
    print_hi('PyCharm')
    config = {'max_new_tokens': 300, 'repetition_penalty': 1.1, 'temperature': 0.2, 'top_k': 40, 'batch_size': 3,
              'top_p': 0.95}
    llm = CTransformers(model=f'{model}', model_type='llama', config=config)
    return (llm(f'''
    [INST]<<SYS>>
You are professional Java Developer
<</SYS>>[/INST]
[INST]
{"Answer the question question: " + prompt+ "base your asnwer on thext from here: " + chunk}
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
