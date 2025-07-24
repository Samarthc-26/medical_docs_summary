import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate



def summarize_pdf(file_path):
    """
    Loads a PDF, extracts its text, and generates a 5-point summary
    using the Groq API.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
        str: The generated summary.
    """
    # Load API Key
    try:
        groq_api_key = st.secrets["GROQ_API_KEY"]
    except KeyError:
        raise ValueError("GROQ_API_KEY not found in Streamlit secrets. Please add it.")

    #Load and Process the PDF

    loader = PyPDFLoader(file_path)
    pages = loader.load()

    # Combine the content of all pages into a single string.
    all_text = " ".join([page.page_content for page in pages])

    # Defining the Prompt Template
    # This template guides the language model to produce a structured summary.
    prompt = '''
You are a highly skilled medical assistant.
Summarize the following medical case record into exactly 5 numbered points.
Do not add any introductions, conclusions, or extra lines like "Here is the summary...".

Your summary must include:
1. Patient demographics (name, age) and primary condition.
2. Key symptoms and critical clinical findings.
3. The final diagnosis.
4. Important treatments, procedures, or medications administered.
5. The patient's outcome and any discharge advice provided.

Text:
{text}
'''
    prompt_template = PromptTemplate.from_template(prompt)

    # Initialize the Language Model
    # We use ChatGroq with the Llama3 70b model for fast and powerful summarization.
    llm = ChatGroq(model='llama3-70b-8192', api_key=groq_api_key)

    #  Create and Run the Chain
    # The LCEL chain pipes the formatted prompt into the language model.
    chain = prompt_template | llm
    result = chain.invoke({'text': all_text})

    return result.content
