import os
import streamlit as st

# Import Ollama LLM from LangChain community package
from langchain_community.llms import Ollama

# Import prompt template to structure input
from langchain_core.prompts import ChatPromptTemplate

# Import output parser to convert model output into string
from langchain_core.output_parsers import StrOutputParser

# Step 1: Create prompt templates
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond clearly to the questions asked."),
        ("user", "Question: {question}")
    ]
)

# Step 2: Streamlit APP UI
st.title("CHITCHAT : LangChain with Gemma model (Ollama)")
input_text = st.text_input("What Questions do you have in your Mind?")

# Step 3: Load Ollama Model
llm = Ollama(model="gemma2:2b")   # ✅ Correct model name

# Convert model output to string
output_parser = StrOutputParser()

# Create LangChain pipeline (Prompts --> Model --> Output parser)
chain = prompt | llm | output_parser

# Initialize session state for history (outside input_text check)
if "history" not in st.session_state:
    st.session_state.history = []

# Run model when user inputs questions
if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)
    # Save both question and response
    st.session_state.history.append((input_text, response))

# Sidebar history (show last 5 Q&A)
st.sidebar.title("History")
for i, (question, answer) in enumerate(st.session_state.history[-5:], start=1):
    st.sidebar.write(f"{i}. Q: {question}")
    st.sidebar.write(f"   A: {answer}")