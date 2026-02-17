import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def enhance_resume(text, job_desc):
    prompt = f"""
    Improve this resume for ATS optimization.
    Job Description:
    {job_desc}

    Resume:
    {text}

    - Improve grammar
    - Add relevant keywords
    - Maintain professional tone
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content
