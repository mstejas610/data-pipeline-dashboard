from pathlib import Path

import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


BASE = Path(__file__).resolve().parent.parent
PROCESSED = BASE / "data" / "processed"

app = FastAPI(title="Data Analytics Platform API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/api/revenue")
def revenue():
    df = pd.read_csv(PROCESSED / "monthly_revenue.csv")
    return df.to_dict(orient="records")


@app.get("/api/top-customers")
def top_customers():
    df = pd.read_csv(PROCESSED / "top_customers.csv")
    return df.to_dict(orient="records")
