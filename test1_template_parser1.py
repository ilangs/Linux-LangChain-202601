from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()

llm = ChatOpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),
    model = os.getenv("MODEL_NAME"), 
    temperature = 0.2
)

result = llm.invoke("AI를 이용하여 2행시를 만들어 줘.").content


