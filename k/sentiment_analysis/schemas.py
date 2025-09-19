from pydantic import BaseModel
from typing import List,Any,Dict

class TextRequest(BaseModel):
    input_text:str
    session_id:str
    
class TextResponse(BaseModel):
    sentiment:List[dict]
    summary: Any
    text: str
    session_id: str