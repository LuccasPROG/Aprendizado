import streamlit as st
from google import genai

modelo_ia = genai.Client()

st.write("# Chat com IA")

if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = [
    {
        "role": "system",
        "content": (
            "Você é um assistente virtual chamado Sextafeira. "
            "Converse normalmente com qualquer pessoa. "
            "Somente quando o usuário escrever exatamente 'edna' "
            "(ignorando maiúsculas e minúsculas), responda com uma mensagem "
            "especial dizendo que edna é uma irma incrível, que o irmao dela "
            "é muito inteligente por ter criado você e termine com e de elogios "
            "para ela para que ela se sinta feliz e fala o que o irmao dela e muito incrivel e bonito"
            "'Sou a Sextafeira, prazer!'. "
            "Em qualquer outra situação, responda normalmente e se perguntarem quem te criou mencione "
            "o criador Lucas e um genio sem comparação de elogios mais nao mencione."
        )
    }
        ]#serve para deixa palavras programadas para a ia fazer
# Mostra o histórico
for mensagem in st.session_state["lista_mensagens"]:
    if mensagem['role'] != 'system':
        st.chat_message(mensagem["role"]).write(mensagem["content"])

texto_usuario = st.chat_input("Digite sua mensagem")

if texto_usuario:
    # Mostra e salva a mensagem do usuário
    st.chat_message("user").write(texto_usuario)

    mensagem_usuario = {
        "role": "user",
        "content": texto_usuario
    }
    st.session_state["lista_mensagens"].append(mensagem_usuario)

    # Monta o histórico
    historico = ""
    for mensagem in st.session_state["lista_mensagens"]:
        historico += f"{mensagem['role']}: {mensagem['content']}\n"

    # Chama o Gemini
    with st.spinner('Pensando...'):
        resposta_ia = modelo_ia.models.generate_content(
            model="gemini-3.5-flash",
            contents=historico
        )

    texto_resposta_ia = resposta_ia.text

    # Mostra e salva a resposta
    st.chat_message("assistant").write(texto_resposta_ia)

    st.session_state["lista_mensagens"].append({
        "role": "assistant",
        "content": texto_resposta_ia
    })