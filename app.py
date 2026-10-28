from langchain_openai import ChatOpenAI
import streamlit as st

st.header('Research Tool')
user_input = st.text_input("Enter your prompt here:")

if st.button("Submit"):
    st.text("some random text")
