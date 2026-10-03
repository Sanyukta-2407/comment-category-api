from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

model = joblib.load("model.pkl")


class CommentInput(BaseModel):
    comment: str
    upvote: int
    downvote: int
    if_1: int
    if_2: int
    race: str
    religion: str
    gender: str
    disability: bool


@app.get("/")
def home():
    return {"message": "Comment Category API is running"}


@app.post("/predict")
def predict(data: CommentInput):
    input_data = pd.DataFrame([data.dict()])

    prediction = model.predict(input_data)

    return {
        "prediction": int(prediction[0])
    }