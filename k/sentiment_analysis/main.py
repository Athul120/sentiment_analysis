from fastapi import FastAPI

import logging
import logger_config
from schemas import TextResponse,TextRequest
from nlp.sentiment import Sentiment
from nlp.summarizer import summarizer
from nlp.language_detect import langtranslator
from nlp.sessions_handler import sessions
from fastapi import APIRouter


app=FastAPI(title="Sentiment analysis model")

@app.post("/sentiment-analysis/",response_model=TextResponse)

def text(payload:TextRequest):
    input_text=payload.input_text
    txt=langtranslator.text_translate(input_text)
    sentiment=Sentiment.analyze_text(txt)
    summary=summarizer(txt)
    session_id=payload.session_id
    sessions.add_to_session(session_id,input_text,sentiment,summary)

    return TextResponse(
        sentiment=sentiment,
        summary=summary,
        text=payload.input_text,
        session_id=payload.session_id
    )


@app.get("/sessions/{session.id}")

def get_session_data(session_id):
    return{"History":sessions.get_session(session_id)}


@app.delete("/sessions/{session_id}")

def delete_session_data(session_id):
    return sessions.clear_session(session_id)


@app.delete("/sessions/")
def clear_all_sessions():
    return sessions.clear_all_sessions()

@app.get("/")

def read_root():
    return{"message":"Text analysis"}   