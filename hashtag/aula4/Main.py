import streamlit as st
from openai import OpenAI





modelo_ia = OpenAI(api_key='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')


st.write('# Chat com IA')

if not 'lista_mensagens' in st.session_state:
    st.session_state['lista_mensagens'] = []


texto_usuario = st.chat_input('Digite sua mensagem')

for mensagem in st.session_state['lista_mensagens']:
    role = mensagem['role']
    content = mensagem['content']
    st.chat_message(role).write(content)
    
# hugging face criar minha propria IA

if texto_usuario:
    st.chat_message('user').write(texto_usuario)
    mensagem_usuario = {'role': 'user', 'content': texto_usuario}
    st.session_state['lista_mensagens'].append(mensagem_usuario)

    resposta_ia = modelo_ia.chat.completions.create(
        messages=st.session_state['lista_mensagens'], 
        model='gpt-4o')

    texto_resposta_ia = resposta_ia.choices[0].message.content

    st.chat_message('assistant').write(resposta_ia)
    mensagem_ia = {'role': 'assistant', 'content': texto_resposta_ia}
    st.session_state['lista_mensagens'].append(mensagem_ia)
