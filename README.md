# 📚 PDF 기반 문서 임베딩 및 자연어 질의 시스템

이 프로젝트는 PDF 문서를 파이썬으로 불러와 텍스트 추출, 임베딩, 벡터 저장소 구축을 거쳐, OpenAI 기반의 LLM으로 자연어 검색(QA)을 수행하는 파이프라인입니다. 특히 **스페인어 PDF 문서**를 처리하고, LLM을 통한 문서 질의 응답 시스템을 구현합니다.

---

## 🔧 기술 스택

* **Python** 3.10+
* **Streamlit** – 비밀 키 관리 및 인터페이스
* **LangChain** – 문서 처리, 임베딩, 검색, QA 체인 구성
* **OpenAI API** – GPT-4 기반 LLM 질의 응답
* **FAISS** – 벡터 저장소 및 검색 엔진
* **PyPDFLoader** – PDF 문서 텍스트 추출

---

## 🗂 프로젝트 구조

```bash
project/
│
├── data/
│   └── el-joven.pdf        # 분석 대상 PDF 문서
│
├── main.py                 # 전체 파이프라인 코드
├── requirements.txt        # 필요한 Python 패키지 목록
└── README.md               # 현재 문서
```

---

## 🚀 실행 방법

1. **필수 패키지 설치**

```bash
pip install -r requirements.txt
```

2. **`.streamlit/secrets.toml` 설정**

OpenAI API 키를 아래처럼 저장합니다:

```toml
[general]
OPENAI_API_KEY = "your_openai_api_key"
```

3. **PDF 임베딩 및 QA 수행**

`main.py`를 실행하면 다음 작업이 수행됩니다:

* PDF 문서 로드 및 텍스트 추출
* OpenAI Embedding으로 벡터화
* FAISS에 벡터 저장소 생성
* GPT-4 모델 기반으로 질의응답 수행

```bash
python main.py
```

---

## 📌 주요 코드 흐름 요약

### 1. PDF 텍스트 추출

```python
from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader("./data/el-joven.pdf")
document = loader.load()
```

### 2. 문서 임베딩

```python
from langchain_community.embeddings import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(document, embeddings)
```

### 3. LLM 기반 질의응답

```python
from langchain_community.chat_models import ChatOpenAI
llm = ChatOpenAI(temperature=0, model_name='gpt-4')

from langchain.chains import RetrievalQA
retriever = db.as_retriever()
qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

query = "Cómo cambia la percepción del protagonista sobre su ciudad al revisitar por segunda vez?"
result = qa({"query": query})
```

---

## 🧠 기대 효과

* 📖 **문서 검색 자동화**: PDF 등 비정형 문서를 기반으로 자연어 질의 가능
* 🤖 **GPT-4 활용**: 고도화된 문맥 이해를 통해 정확한 응답 제공
* 🧩 **확장 가능성**: 다양한 언어, 문서 형식 및 검색 조건에 유연하게 적용 가능

---

## 📝 TODO (확장 아이디어)

* [ ] Streamlit 기반 인터랙티브 UI 개발
* [ ] 멀티 PDF 처리 지원
* [ ] 문서 섹션별 요약 및 하이라이트 기능
* [ ] Chat history 기반 follow-up 질문 처리

---

## 📄 License

MIT License (자유롭게 사용, 수정, 배포 가능)

---

## 🙋‍♂️ Contact

궁금한 점이나 피드백은 언제든지 Issue나 PR로 남겨주세요.
