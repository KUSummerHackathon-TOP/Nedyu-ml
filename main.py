from typing import Optional
from fastapi import FastAPI
from torchmetrics.text import bert, rouge

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*",
]

USEBERT = False

if USEBERT:
    bertscore = bert.BERTScore(
        model_name_or_path="distilbert-base-uncased", device="cuda:0"
    )
else:
    bertscore = None

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

    if USEBERT:
        score = bertscore(summary, orginal)
        score = score["precision"]
    else:
        scorer = rouge.ROUGEScore()
        score = scorer(summary, orginal)
        score = score["rouge1_precision"].item()
    print(score)
    return score
