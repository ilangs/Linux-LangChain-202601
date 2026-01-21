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


prompt = PromptTemplate.from_template(
    '''
    AI를 주제로 하이쿠를 작성해 줘
    조건: 의미있는 문장으로 작성해 줘
    스타일 : 3행시로 만들어 줘
    '''
)


chain = prompt | llm | StrOutputParser()
result = chain.invoke({})
print(result)

