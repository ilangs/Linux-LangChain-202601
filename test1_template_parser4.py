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


# # prompt1
# prompt1 = "LLM이란 무엇인가?"

# # prompt2 (style)
# prompt2 = "2행으로 구성해 줘"

# # prompt3
# prompt3 = PromptTemplate.from_template("{base}\n{style}\n{length}")


# # 여러 프롬프트를 연결 (format 속성)
# resultPrompt = prompt3.format(base=prompt1, style=prompt2, length="15")


# chain = PromptTemplate.from_template(resultPrompt) | llm | StrOutputParser()
# result = chain.invoke({})
# print(result)


# 프롬프트1
prompt = PromptTemplate.from_template(
    "AI 를 주제로 하이쿠를 작성해줘."
)
# 프롬프트2 (syle)
prompt2 = PromptTemplate.from_template(
    "3행으로 구성해줘."
)

prompt3 = PromptTemplate.from_template(
    "{base}\n{style}"
)
# 여러 프롬프트를 연결 하기 format(속성)
resultPrompt = prompt3.format(base=prompt.format(), style=prompt2.format())

# chain은 체인은 Runnable만으로 구성. 문자열 x
chain = RunnableLambda(lambda _: resultPrompt) | llm | StrOutputParser()
result2 = chain.invoke({})
print(result2)

'''
PromptTemplate의 메서드 역할
생성 : From_template()
문자열 변환: format(), 프롬프트 템플릿에 뱐수를 전달 가능
PromptTemplate은 Runnable 클래스를 상속받은 Runnable 타입
다시말해 Langchain은 Runnable을 상속받은 PromptTemplate 사용.
문자열은 체인으로 묶는 것 불가능, 체인에 묶으려면 형변환 필수.
RunnableLambda로 변환 히야 한다.
그러나, 권장하는 변수 전달 방법은 체인을 실행시 invoke({})의 dict 형식의 인자로 전달.
JSON 문자열 처럼 키도 str로 감싼다.
'''

