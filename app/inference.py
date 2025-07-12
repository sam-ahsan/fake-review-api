import joblib
import os
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer

model_path = Path(__file__).resolve().parent.parent / "model" / "fake_review_model.pkl"
model = joblib.load(model_path)

def predict_review(text: str):
    vectorizer = model['vectorizer']
    classifier = model['model']
    X = vectorizer.transform([text])
    proba = classifier.predict_proba(X)[0]
    label = classifier.classes_[proba.argmax()]
    confidence = float(proba.max())
    return {"prediction": label, "confidence": confidence}
