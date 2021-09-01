from typing import List, Dict, Optional #python std lib for datatypes
from ml import nlp
from fastapi import FastAPI, Query
from pydantic import BaseModel

"""
How to run: uvicorn app:app --reload
Live at: http://127.0.0.1:8000/
Swagger doc: http://127.0.0.1:8000/docs
API documentation: http://127.0.0.1:8000/redoc
"""

app = FastAPI()

@app.get("/analyze/{article_id}")
def analyze_article(article_id: int, q: str = None):
    count = 0
    if q:
        doc = nlp(q)
        count = len(doc.ents)
    return {"id": article_id, "query": q, "count": count}

class Article(BaseModel):  #to use type hint with fastapi our class should inherit basemodel
    content: str = Query(None, max_length = 500)  #specify max length of request
    # comments: list = []
    comments: List[str] #std way of saying we need a list of strings
    messages: Optional[List[dict]] # Message is an optional item

@app.post("/analyze/")
def analyze_article(article: Article):
    doc = nlp(article.content)
    ents = []
    for ent in doc.ents:
        ents.append({ent.text: ent.label_})
    return {"message": article.content, "comments": article.comments, "ents": ents}

@app.post("/analyzemulti/")
async def analyze_article_multiple(articles: List[Article]):   #list of article class
    #docstrings are extracted by fast api and shown in the live doc
    #can add markdown in docstrng too
    """
    Analyze articles with the help of **spacy** 
    """
    ents = []
    for article in articles:
        doc = nlp(article.content)
        for ent in doc.ents:
            ents.append({ent.text: ent.label_})
    return { "ents": ents}

