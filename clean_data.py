from pathlib import Path

import pandas as pd


BASE = Path(__file__).parent
RAW = BASE / "data" / "raw"
OUT = BASE / "data" / "processed"


def parse_date(value):
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%m-%d-%Y"):
        try:
            return pd.to_datetime(value, format=fmt)
        except (TypeError, ValueError):
            continue
    return pd.NaT


def clean_customers():
    df = pd.read_csv(RAW / "customers.csv")

    print("Cleaning customers...")

    df["signup_date"] = df["signup_date"].apply(parse_date)
    df = df.sort_values("signup_date").drop_duplicates("customer_id", keep="last")

    df["email"] = df["email"].fillna("").str.strip().str.lower()
    df["is_valid_email"] = df["email"].str.contains(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", na=False)

    df["name"] = df["name"].fillna("").str.strip()
    df["region"] = df["region"].fillna("Unknown").str.strip()

    df.to_csv(OUT / "customers_clean.csv", index=False)


def clean_orders():
    df = pd.read_csv(RAW / "orders.csv")

    print("Cleaning orders...")

    df["order_date"] = df["order_date"].apply(parse_date)
    df = df.dropna(subset=["customer_id", "order_id"], how="all")

    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df["amount"] = df.groupby("product")["amount"].transform(lambda values: values.fillna(values.median()))

    df["status"] = df["status"].fillna("").str.strip().str.lower().replace(
        {
            "done": "completed",
            "canceled": "cancelled",
        }
    )
    df["order_year_month"] = df["order_date"].dt.to_period("M").astype(str)

    df.to_csv(OUT / "orders_clean.csv", index=False)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    clean_customers()
    clean_orders()
    print("Data cleaning complete")
