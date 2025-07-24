# 🩺 Medical PDF Summarizer using LangChain, Groq & Streamlit

This project is a **Medical Document Summarization Tool** built to help **doctors and healthcare professionals** quickly extract the **core details** from lengthy case records or medical PDFs. It uses **LangChain**, **Groq API**, and **LLaMA model** to generate clear 5-point summaries.

---

## 🚀 Features

- 📄 Upload any medical PDF
- 🤖 Automatically generates a 5-point summary using LLM
- 🧠 Built with LangChain + Groq + LLaMA 3.3 70B Versatile
- 🌐 Deployable on Streamlit Cloud
- 🔐 API key securely stored via `.env` or Streamlit secrets

---

## 🧠 Summary Format

Each summary includes:

1. Patient name, age, and condition  
2. Main symptoms and key findings  
3. Final diagnosis  
4. Important treatments given  
5. Outcome and discharge advice (if available)  

---

## 📦 Tech Stack

- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [Groq API](https://groq.com/)
- [LLaMA Model (via Groq)](https://www.groq.com/groqcloud)
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/)
- [Python dotenv](https://pypi.org/project/python-dotenv/)

---

## 🛠️ How to Run Locally

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/pdf-medical-summarizer.git
   cd pdf-medical-summarizer
