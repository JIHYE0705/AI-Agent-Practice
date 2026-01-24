import streamlit as st

from ai_clients.ollama_client import OllamaClient

ollama = OllamaClient()

st.title('💭Chatbot')

if 'messages' not in st.session_state:
    st.session_state['messages'] = [{'role': 'assistant', 'content': 'How can I help you?'}]

for msg in st.session_state.messages:
    st.chat_message(msg['role']).write(msg['content'])

if prompt := st.chat_input():
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    st.chat_message('user').write(prompt)
    response = ollama.chat(messages=st.session_state.messages)

    msg = response['message']['content']
    st.session_state.messages.append({'role': 'assistant', 'content': msg})
    st.chat_message('assistant').write(msg)
