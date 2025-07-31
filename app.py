from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
import os
from langchain.schema import HumanMessage, SystemMessage, AIMessage

# Load .env variables
load_dotenv()

# Streamlit UI setup
st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, Let's Chat")

# Initialize the Gemini model
chat = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=1)

# Initialize message history in session
if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content="You are a comedian AI assistant.")
    ]

# Function to get chatbot response
def get_chatmodel_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer = chat.invoke(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content

# User input
user_input = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

# On submit
if submit:
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        response = get_chatmodel_response(user_input)
        st.subheader("The Response is:")
        st.write(response)
