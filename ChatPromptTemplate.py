from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

# 1. 구조화된 템플릿 정의 (표준)
prompt = ChatPromptTemplate.from_messages([
    ("system", "너는 {topic} 분야의 전문가야. 답변은 {style}하게 해줘."),
    ("user", "{question}")
])

# 2. 체인 결합
chain = prompt | llm | StrOutputParser()

# 3. 실행 (데이터 주입)
result = chain.invoke({
    "topic": "인공지능",
    "style": "시적인 3줄 문장, 줄마다 줄바꿈",
    "question": "AI의 미래에 대해 말해줘"
})

print(result)
