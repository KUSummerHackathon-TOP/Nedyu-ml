from typing import Optional
from fastapi import FastAPI
from torchmetrics.text import bert, rouge

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*",
]

bertscore = bert.BERTScore(model_name_or_path="distilbert-base-uncased", device = "cuda:0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/textsim")
def text_similarity(summary: str, orginal: str):
    summary = summary.replace("\n", " ")

    score = bertscore(summary, orginal)
    print(score)
    return score["precision"]
