from pydantic import BaseModel

class ReviewRequest(BaseModel):
    text: str
    
class ReviewResponse(BaseModel):
    prediction: str
    confidence: float
