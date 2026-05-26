import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Streamlit page config
st.set_page_config(page_title="Groq AI Chatbot", page_icon="🤖")

st.title("🤖 Groq AI Chatbot")
st.write("Assignment 39 - Real GenAI Deployment using Groq API")

# Get API key
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    st.error("Groq API Key not found!")
    st.stop()

# Create client
client = Groq(api_key=groq_api_key)

# User input
user_input = st.text_area("Ask anything:")

if st.button("Generate Response"):

    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        try:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "user", "content": user_input}
                ]
            )

            answer = response.choices[0].message.content

            st.success("Response Generated!")
            st.write(answer)

        except Exception as e:
            st.error(f"Error: {e}")
