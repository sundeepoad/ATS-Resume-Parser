# matcher.py
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
import nltk


#nltk.download('stopwords')
#stop_words = set(stopwords.words('english'))
#print(stop_words)

def extract_keywords(text):
    # 
    words = re.findall(r"\b\w{3,}\b", text.lower())  ## will return words with atleast 3 chars.
    
    common_words = set([
        "with", "and", "the", "for", "you", "are", "that", "your", "will",
        "have", "this", "job", "from", "our", "not", "all", "can", "has", "any"
    ])
    return set([word for word in words if word not in stop_words])

def calculate_match_score(resume_text, job_text):
    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_text)

    matched = resume_keywords & job_keywords
    missing = job_keywords - resume_keywords

    score = int(len(matched) / len(job_keywords) * 100) if job_keywords else 0

    return {
        "score": score,
        "matched": list(matched),
        "missing": list(missing)
    }
