
import streamlit as st
from ai_utils import get_gemini_response

def set_page_config():
    st.set_page_config(page_title="Garagemate AI", page_icon=":car:", layout="wide")
    
    # Custom CSS for gray and black theme
    st.markdown("""
    <style>
    .big-font {
        font-size:36px !important;
        font-weight: bold;
        color: #FF4500;
        text-align: center;
    }
    .stApp {
        background-color: #2C2C2C;
        color: #E0E0E0 !important;
    }
    body {
        color: #E0E0E0;
    }
    p, .stMarkdown, .stText {
        color: #E0E0E0 !important;
    }
    .stButton>button {
        background-color: #FF4500;
        color: white;
    }
    .stSelectbox {
        background-color: #3C3C3C;
    }
    </style>
    """, unsafe_allow_html=True)

def display_chat_history():
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("What car-related question do you have?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        full_prompt = f"""You are an advanced garage AI assistant. Provide detailed information, advice, or insights on the following car-related query:

        {prompt}

        Consider various aspects such as car maintenance, repairs, costs, and best practices. Include relevant statistics or data if applicable.

        Remember to include a disclaimer that this information is for educational purposes only and not a substitute for professional mechanic advice or service."""

        response = get_gemini_response(full_prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})