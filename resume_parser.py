import fitz
from docx import Document

def parse_pdf(file):
    text = ""
    doc = fitz.open(stream=file.read(), filetype="pdf")
    for page in doc:
        text += page.get_text()
    return text

def parse_docx(file):
    doc = Document(file)
    return "\n".join([p.text for p in doc.paragraphs])
