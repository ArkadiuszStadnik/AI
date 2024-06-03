from main import print_hi
from langchain_community.llms import CTransformers


def chat_with_model(prompt ,model):
    print_hi('PyCharm')
    config = {'max_new_tokens': 300, 'repetition_penalty': 1.1, 'temperature': 0.2, 'top_k': 40, 'batch_size': 3,
              'top_p': 0.95}
    llm = CTransformers(model=f'{model}', model_type='llama', config=config)
    print(llm(f'''
    [INST]<<SYS>>
You are professional Python Developer
<</SYS>>[/INST]
[INST]
{prompt}
[/INST]
 '''))


if __name__ == '__main__':
    print(chat_with_model("Tell me your name","codellama-7b-instruct.Q4_K_M.gguf"))