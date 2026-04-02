import pandas as pd
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path


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


def load_report(filename):
    try:
        df = pd.read_csv(PROCESSED / filename)
    except FileNotFoundError as exc:
        raise HTTPException(status_code=404, detail=f"{filename} not found") from exc
    return df.to_dict(orient="records")


@app.get("/api/revenue")
def revenue():
    return load_report("monthly_revenue.csv")


@app.get("/api/top-customers")
def top_customers():
    return load_report("top_customers.csv")


@app.get("/api/categories")
def categories():
    return load_report("category_revenue.csv")


@app.get("/api/regions")
def regions():
    return load_report("regional_revenue.csv")
