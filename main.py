import math
from typing import Optional
from fastapi import FastAPI
from torchmetrics.text import bert, rouge

from fastapi.middleware.cors import CORSMiddleware
from fuzzywuzzy import fuzz

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


@app.get("/summary_score")
def text_similarity(summary: str, original: str):
    summary = summary.replace("\n", " ")

    if USEBERT:
        score = bertscore(summary, original)
        score = score["precision"]
    else:
        scorer = rouge.ROUGEScore()
        score = scorer(summary, original)
        score = score["rouge1_precision"].item()
    print(score)

    score = 4 * score - 0.3 * fuzz.ratio(summary, original) / 100 - len(summary) / 50
    score = 1 / (1 + math.exp(-score))

    return {"score": score}
