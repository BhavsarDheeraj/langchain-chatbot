import requests
import streamlit as st


def get_openai_response(input_text):
    response = requests.post(
        "http://localhost:8000/teacher/openai/invoke",
        json={"input": {"query": input_text}},
    )
    return response.json()["output"]["content"]


def get_llama2_response(input_text):
    response = requests.post(
        "http://localhost:8000/teacher/llama2/invoke",
        json={"input": {"query": input_text}},
    )
    return response.json()["output"]


# Streamlit
st.title("Machine Learning Teacher")
input_text = st.text_input("Ask me anything about Machine Learning")
llm = st.radio(
    "What do you want to use?",
    ["OpenAI", "LLama2"],
)

if input_text:
    if llm == "OpenAI":
        st.write(get_openai_response(input_text))
    elif llm == "LLama2":
        st.write(get_llama2_response(input_text))
