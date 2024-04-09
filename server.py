from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models.openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv
from langchain_community.llms.ollama import Ollama

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2")

app = FastAPI(
    title="Langchain Chat Server",
    version="1.0",
)

add_routes(app, ChatOpenAI(), path="/chat")

openai_model = ChatOpenAI()
llama2_model = Ollama(model="llama2")

prompt = "You are a helpful teacher and an expert machine researcher. Please help the student and explain in a very intuitive, interactive and simple manner. Query : {query}"

prompt_openai = ChatPromptTemplate.from_template(prompt)
prompt_llama2 = ChatPromptTemplate.from_template(prompt)

add_routes(app, prompt_openai | openai_model, path="/teacher/openai")
add_routes(app, prompt_llama2 | llama2_model, path="/teacher/llama2")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
