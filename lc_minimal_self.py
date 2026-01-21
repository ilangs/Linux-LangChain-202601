# 과제 : 안보고 칠 때까지 반복횟수, 총소요 시간을 카페에 제출
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

parser = StrOutputParser()

prompt_map ={
    "1" : ("요약", "다음의 내용을 한 문장으로 요약 해 주세요.\n내용: {text}"),
    "2" : ("키워드", "다음의 내용에서 핵심 키워드 5개를 뽑아 주세요.\n내용: {text}"),
    "3" : ("답변", "다음 질문에 대해 3문장 이내로 답변 해 주세요.\n질문: {text}")
}

print("1)요약   2)키워드   3)답변")
sel = input("선택 (1~3): ").strip()

if sel not in prompt_map :
    raise SystemExit ("잘못된 선택")

name, template = prompt_map[sel]
prompt = PromptTemplate.from_template(template)

chain = prompt | llm | parser

text = input(f"[{name}] 내용 입력: ").strip()
print(chain.invoke({"text":text}))
