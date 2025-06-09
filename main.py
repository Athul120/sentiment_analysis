from fastapi import FastAPI
from schemas import TextResponse,TextRequest
from nlp.languagedetect import analyze_language
from nlp.sentiment import analyze_text
from nlp.summary import summary_text


app=FastAPI()

@app.post("/sentiment-analysis/",response_model=TextResponse)
def text(payload:TextRequest):
    text=payload.text
    sentiment=analyze_text(text)


    summary=summary_text(text)
    language=analyze_language(text)

    return TextResponse(
        sentiment=sentiment,
        language=language,
        text=payload.text 
    )

@app.get("/")

def read_root():
    return{"message":"Text analysis"}