import streamlit as st
import tempfile
import os
from summariser_pdf import summarize_pdf

# --- Page Configuration ---
st.set_page_config(page_title="Medical PDF Summarizer", layout="centered", page_icon="📋")
st.title("📋 Medical PDF Summarizer")
st.write("Upload a medical case record to generate a 5-point summary using Groq's Llama 3.")

# --- File Uploader ---
uploaded_file = st.file_uploader("Upload a medical PDF", type="pdf")

if uploaded_file is not None:
    # Create a temporary file to store the uploaded content
    # Using a 'with' statement ensures the file is handled correctly
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        file_path = tmp_file.name

    # --- Summarize Button ---
    if st.button("Generate Summary"):
        with st.spinner("Analyzing document and generating summary..."):
            try:
                # Call the summarization function
                summary = summarize_pdf(file_path)
                st.subheader("📝 Summary")
                st.markdown(summary)
            except Exception as e:
                st.error(f"❌ An error occurred: {e}")
            finally:
                # Clean up the temporary file AFTER the summarization is done
                os.remove(file_path)
