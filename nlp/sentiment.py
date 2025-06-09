from transformers import pipeline


sentiment_model=pipeline("sentiment-analysis")
model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
revision="714eb0f",
device=-1

def analyze_text(text:str)->str:
    result=sentiment_model(text)[0]
    return result['label'].lower()
