from fastapi import FastAPI, UploadFile, Form
from resume_parser import parse_pdf, parse_docx
from ats_score import calculate_ats_score
from ai_enhancer import enhance_resume
from resume_generator import generate_word, generate_pdf

app = FastAPI()

@app.post("/process/")
async def process_resume(
    file: UploadFile,
    job_desc: str = Form(...)
):
    if file.filename.endswith(".pdf"):
        resume_text = parse_pdf(file)
    else:
        resume_text = parse_docx(file)

    original_score = calculate_ats_score(resume_text, job_desc)
    enhanced_text = enhance_resume(resume_text, job_desc)
    enhanced_score = calculate_ats_score(enhanced_text, job_desc)

    word = generate_word(enhanced_text)
    pdf = generate_pdf(enhanced_text)

    return {
        "original_score": original_score,
        "enhanced_score": enhanced_score,
        "word_file": word,
        "pdf_file": pdf
    }
