import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

# 🔑 API keys (hardcoded)
GOOGLE_API_KEY = "AIzaSyBAZIiQ6ODY5VqW5QN4TC69U43SiJzy2r4"
LANGCHAIN_API_KEY = "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"
LANGCHAIN_PROJECT = "genaitut"

# ✅ Initialize Gemini model with API key
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",   # ⚡ switch to flash model
    api_key=GOOGLE_API_KEY,
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)


# ✅ Define prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful chatbot."),
        ("human", "Question: {question}")
    ]
)

# ✅ Streamlit UI
st.title("🤖 LangChain Demo with Gemini")
input_text = st.text_input("Enter your question here")

# ✅ Output parser
output_parser = StrOutputParser()

# ✅ Create chain (Prompt → LLM → Output)
chain = prompt | llm | output_parser

if input_text:
    try:
        response = chain.invoke({"question": input_text})
        st.write(response)
    except Exception as e:
        st.error(f"⚠️ Error: {e}")

# ✅ Debug info (just to confirm API keys loaded)
st.sidebar.title("🔑 Debug Info")
st.sidebar.write(f"GOOGLE_API_KEY loaded: {GOOGLE_API_KEY[:6]}...***")
st.sidebar.write(f"LANGCHAIN_PROJECT: {LANGCHAIN_PROJECT}")
