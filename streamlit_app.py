import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate
from langchain.schema import HumanMessage

# Streamlit 설정
st.title('텍스트 요약 앱')

# 사이드바에서 OpenAI API 키 입력
oai_key = st.sidebar.text_input("OpenAI API Key", type="password")

if oai_key:
    # Langchain 모델 설정
    llm = ChatOpenAI(model_name="gpt-4o-mini", openai_api_key=oai_key)
    
    # 텍스트 입력
    user_input = st.text_area("요약할 텍스트를 입력하세요:")

    if st.button("요약하기"):
        if user_input:
            # 요약 프롬프트 설정
            prompt = PromptTemplate(template="다음 텍스트를 간단히 요약하세요: {text}", input_variables=["text"])
            summary_prompt = prompt.format(text=user_input)
            
            # 요약 생성
            response = llm([HumanMessage(content=summary_prompt)])
            summary = response.content
            
            # 결과 출력
            st.subheader("요약 결과:")
            st.write(summary)
        else:
            st.warning("요약할 텍스트를 입력해주세요.")
else:
    st.warning("API 키를 입력해주세요.")