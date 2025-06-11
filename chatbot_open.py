"""데이터 연결 작업
1. 데이터 가져오기 >> pdf를 파이썬이 읽을 수 있는 형태로 추출
2. 문서를 변환 >> 추출된 문서를 변환
3. 문서 임베딩 >> 변홚된 문서를 컴퓨터가 읽을 수 있는 숫자형태로 임베딩
4. 벡터 저장소 >> 임베딩된 데이터를 벡터 저장소에 저장
** 벡터 저장소는 임베딩된 데이터를 저장하는 기능뿐만 아니라 검색하는 기능도 있음
"""
import streamlit as st
#1. pdf 파일 불러오기
from langchain_community.document_loaders import PyPDFLoader

#pdf 로더 설정 및 문서열기
loader = PyPDFLoader("./data/el-joven.pdf")
document = loader.load()

#pdf가 잘 로드 됐는지 확인
#pdf의 6번째 페이지에서 5000글자 읽기
print(document[5].page_content[:5000])

#3. 임베딩
import os
os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']

#from langchain_community.embeddings import FAISS
from langchain_community.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()

#test
text='Extudio coreano en la universidad. Mi universidad está en Seúl.'
text_embedding = embeddings.embed_query(text)
print(text_embedding)

#4. el-joven pdf 파일을 임베딩 후 벡터저장소에 저장
db = FAISS.from_documents(document, embeddings)

"""
데이터를 활용한 검색기 만들기
"""

from langchain_community.chat_models import ChatOpenAI
llm=ChatOpenAI(temperature=0, model_name='gpt-4')

from langchain.chains import RetrievalQA #우리가 만드는 모델이 추론을 할 수 있게 하는 모듈
retriever = db.as_retriever() #쿼리(질문)에 대한 답을 추론할 때 위에서 만든 벡터 저장소를 활용하게 함

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever = retriever
) #추론 방법을 정한 추론 모델 설정

query = ("Cómo cambia la percepción del protagonista sobre su ciudad al revisitar por segunda vez?")
#질문 내용: 주인공이 두번째로 자신의 도시를 방문했을 때, 도시에 대한 그의 인식은 어떻게 변화했는가?
result=qa({"query": query})
print(result['result'])