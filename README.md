# 📚 Chatbot: *El joven* by Salvador Novo

This Streamlit-based chatbot answers questions about *El joven* (1923), a short novel by Salvador Novo — a foundational text in 20th-century Mexican literature. The chatbot uses OpenAI's GPT-4 API (via LangChain) to provide context-aware, literary responses to user queries.

---

## 🔍 About the Project

This chatbot was developed as a final project for the course:

**Spanish Natural Language and Speech Processing**  
(스페인어 자연어 및 음성 데이터 처리)  
at **Korea University**

---

## 🧠 Key Features

- Ask literary questions about *El joven* (themes, characters, style, etc.)
- Get concise or detailed literary responses powered by ChatGPT (GPT-4)
- Designed for Spanish-language literary education and research
- Simple and intuitive web UI via Streamlit

—

## 🚀 How to Use

### 🖥 Run Locally

```bash
git clone https://github.com/yourusername/open-projects-chatbot.git
cd open-projects-chatbot

# Install dependencies
pip install -r requirements.txt

# Create a secrets file for your OpenAI key
mkdir .streamlit
echo 'OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxx"' > .streamlit/secrets.toml

# Run the app
streamlit run Open-projects-chatbot.py
