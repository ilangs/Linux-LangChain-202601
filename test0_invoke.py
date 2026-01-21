from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)


result = llm.invoke("AI를 주제로 한 한국어 하이쿠를 작성하세요.")
print(result.content)
