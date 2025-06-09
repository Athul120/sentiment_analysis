from transformers import pipeline

summarizer = pipeline("summarization")

def summary_text(text: str) -> str:
    if len(text.split()) < 30:
        return text
    summary = summarizer(text, max_length=60, min_length=10, do_sample=False)
    return summary[0]['summary_text']
