import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
import re

load_dotenv()

st.title("My ChatBot")
if "messages" not in st.session_state :
    st.session_state.messages=[]
client = OpenAI()


prompt = st.chat_input("무엇이든 물어보십시오.")
if prompt:
    response = client.responses.create(
    model="gpt-5.5",
    input=prompt
    )
    print(response.output_text)
    st.session_state.messages.append({'role':'user','content':prompt})
    st.session_state.messages.append({'role':'ai','content':{response.output_text}})
    
    for message in st.session_state.messages :
        with st.chat_message(message['role']) : 
            # clean_text =re.sub(r"[\{|\}]","",message["content"]) 
            st.write(f"{message["content"]}")