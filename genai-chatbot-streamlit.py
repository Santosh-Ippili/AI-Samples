import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq client
groqClient = Groq(api_key=api_key)

# Streamlit page setup
st.set_page_config(page_title="Biryanis & More Chatbot", page_icon="🍛")

st.title("🍛 Biryanis and More – AI Assistant")
st.write("Ask anything about Biryanis and More Restaurant in Toronto.")

# Initialize chat history in Streamlit session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant specialized in providing information about Biryanis and More Restaurant in Toronto."
        }
    ]

# Display previous messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    elif msg["role"] == "assistant":
        st.chat_message("assistant").write(msg["content"])

# User input box
prompt = st.chat_input("Ask something...")

if prompt:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Call Groq API
    response = groqClient.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=st.session_state.messages
    )

    reply = response.choices[0].message.content

    # Display assistant reply
    st.chat_message("assistant").write(reply)

    # Save assistant message
    st.session_state.messages.append({"role": "assistant", "content": reply})
