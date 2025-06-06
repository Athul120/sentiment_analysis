from langdetect import detect

def analyze_language (text:str)->str:
    try:
        return(detect(text))
    except:
        return "unknown"