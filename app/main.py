from fastapi import FastAPI
from app.schemas import ReviewRequest, ReviewResponse
from app.inference import predict_review

app = FastAPI()

@app.post("/predict", response_model=ReviewResponse)
def predict(review: ReviewRequest):
    return predict_review(review.text)

@app.get("/")
def root():
    return {"message": "Welcome to the Fake Review Detector API"}