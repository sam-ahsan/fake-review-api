from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

texts = ["This product is great", "Worst purchase ever", "Amazing value", "Fake review", "Terrible and fake"]
labels = ["real", "real", "real", "fake", "fake"]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)

# Save both together
joblib.dump({"vectorizer": vectorizer, "model": model}, "model/fake_review_model.pkl")
