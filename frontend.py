# Step1: Setup Streamlit
import streamlit as st
import requests

BACKEND_URL="http://localhost:8000/ask"
st.set_page_config(page_title="AI Mental Health Therapist", layout="wide")
st.title("🧠 NeuroNest – AI Mental Health Therapist")
st.markdown("Your personal AI-powered mental health companion. Talk to me about anything on your mind.")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []



# Step2: User is able to ask questions
user_input = st.chat_input("What's on your mind today?")
if user_input:
    # Append user message
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # AI agent exists here
    response = requests.post(BACKEND_URL, json={"message": user_input})
    st.session_state.chat_history.append({"role": "assistant", "content": f'{response.json()["response"]} WITH TOOL: [{response.json()["tool_called"]}]'})


# Step3: Display chat history
for message in st.session_state.chat_history:
    if message["role"] == "user":
        st.chat_message("user").markdown(message["content"])
    else:
        st.chat_message("assistant").markdown(message["content"])
#

