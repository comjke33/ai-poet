from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from dotenv import load_dotenv

# .env 파일 내용 불러오기
load_dotenv()

# ChatOpenAI 초기화
llm = init_chat_model("gpt-4o-mini", model_provider="openai")

# 프롬프트 템플릿 생성
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{input}")
])

# 문자열 출력 파서
output_parser = StrOutputParser()

# LLM 체인 구성
chain = prompt | llm | output_parser

# 체인 테스트용 호출
content = "코딩"
result = chain.invoke({"input": content + "에 대한 시를 써줘"})
print(result)

# Streamlit UI
# st.title("인공지능 시인")
title = st.text_input("Movie title", "Life of Brian")
st.write("The current movie title is", title)

content = st.text_input("시의 주제를 입력해주세요")

if st.button("시 작성 요청하기"):
	with st.spinner('Wait for it...'):
		result = chain.invoke({"input": content + "에 대한 시를 써줘"})
		st.write(result)
