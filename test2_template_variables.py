from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

prompt = PromptTemplate.from_template(
    '''
    주제: {topic}\n
    형식: {style}\n
    길이: {length}\n
    요청: 한국어로 AI의 미래를 작성해 줘.
    '''
)

chain = prompt | llm | StrOutputParser()

# invoke에서는 json으로 전달
result = chain.invoke({"topic": "인공지능", "style": "차분하고 서정적", "length": "3줄"})
print(result)
