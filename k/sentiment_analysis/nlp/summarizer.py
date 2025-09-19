from transformers import pipeline
import logging
from typing import Any

logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)


model_summarizer = pipeline("summarization", model="facebook/bart-large-cnn")#sshleifer/distilbart-cnn-12-6
logger.info("Summarization model loaded sucessfully")

def summarizer(input_text:str)->str:
    text_leangth=len(input_text)
    if text_leangth<=30:
        summary=input_text
        logger.info("Text less than 30 characters displaying without summarizing")
    
    else:
        summary=model_summarizer(input_text,max_length=80, min_length=10)

    return summary
