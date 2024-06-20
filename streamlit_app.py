import streamlit as st
import fitz  # PyMuPDF
from transformers import pipeline

# Initialize the question-answering model
qa_model = pipeline("question-answering")

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

st.title("PDF Question Answering")

pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])
if pdf_file:
    context = extract_text_from_pdf(pdf_file)
    st.write("Extracted Text:")
    st.write(context)

    question = st.text_input("Ask a question about the PDF:")
    if question:
        answer = qa_model(question=question, context=context)
        st.write("Answer:")
        st.write(answer['answer'])
