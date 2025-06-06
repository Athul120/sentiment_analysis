from pydantic import BaseModel
from typing import List

class TextRequest(BaseModel):
    text:str

class TextResponse(BaseModel):
    sentiment:str
    language: str
