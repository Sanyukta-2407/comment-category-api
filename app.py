from fastapi import FastAPI
import joblib

app = FastAPI()

model = joblib.load("model.pkl")


@app.get("/")
def home():
    return {"message": "Comment Category API is running"}