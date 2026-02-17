from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_ats_score(resume_text, job_desc):
    vect = TfidfVectorizer(stop_words="english")
    tfidf = vect.fit_transform([resume_text, job_desc])
    score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
    return round(score * 100, 2)
