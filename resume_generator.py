from docx import Document
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_word(text):
    doc = Document()
    doc.add_paragraph(text)
    file_path = "final_resume.docx"
    doc.save(file_path)
    return file_path

def generate_pdf(text):
    file_path = "final_resume.pdf"
    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4
    y = height - 40

    for line in text.split("\n"):
        c.drawString(40, y, line)
        y -= 15
        if y < 40:
            c.showPage()
            y = height - 40

    c.save()
    return file_path
