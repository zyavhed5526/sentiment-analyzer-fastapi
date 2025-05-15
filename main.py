from fastapi import FastAPI
from pydantic import BaseModel
from textblob import TextBlob

app = FastAPI()

class Sentence(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Welcome to the Sentiment Analyzer API!"}

@app.post("/analyze")
def analyze_sentiment(sentence: Sentence):
    blob = TextBlob(sentence.text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "positive"
    elif polarity < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return {
        "text": sentence.text,
        "sentiment": sentiment,
        "polarity_score": polarity
    }
