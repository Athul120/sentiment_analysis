import logging
from transformers import pipeline
from typing import Any,List


logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)

sentiment_model=pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest")
logger.info("sentiment model loaded sucessfully")


class Sentiment_analysis:

    def analyze_text(self,input_text)->List[dict]:
        """For sentiment analysis takes text as input"""
        result=sentiment_model(input_text)
        log_results=sentiment_model(input_text,top_k=None)
        logging.info(f"Identified sentiments: {log_results}")
        return result
    
Sentiment=Sentiment_analysis()

