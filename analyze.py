from pathlib import Path

import pandas as pd


BASE = Path(__file__).parent
RAW = BASE / "data" / "raw"
PROCESSED = BASE / "data" / "processed"


def load_data():
    customers = pd.read_csv(PROCESSED / "customers_clean.csv")
    orders = pd.read_csv(PROCESSED / "orders_clean.csv")
    products = pd.read_csv(RAW / "products.csv")
    return customers, orders, products


def main():
    customers, orders, products = load_data()

    orders["order_date"] = pd.to_datetime(orders["order_date"], errors="coerce")

    orders_with_customers = orders.merge(customers, on="customer_id", how="left")
    full_data = orders_with_customers.merge(
        products,
        left_on="product",
        right_on="product_name",
        how="left",
    )

    # Only completed orders contribute to revenue calculations.
    completed = full_data[full_data["status"] == "completed"].copy()

    monthly = (
        completed.groupby("order_year_month", dropna=False)["amount"]
        .sum()
        .reset_index()
        .sort_values("order_year_month")
    )
    monthly.to_csv(PROCESSED / "monthly_revenue.csv", index=False)

    category_revenue = (
        completed.groupby("category", dropna=False)["amount"]
        .sum()
        .reset_index()
        .sort_values(by="amount", ascending=False)
    )
    category_revenue.to_csv(PROCESSED / "category_revenue.csv", index=False)

    regional_revenue = (
        completed.groupby("region", dropna=False)["amount"]
        .sum()
        .reset_index()
        .sort_values(by="amount", ascending=False)
    )
    regional_revenue.to_csv(PROCESSED / "regional_revenue.csv", index=False)

    top_customers = (
        completed.groupby(["customer_id", "name", "region"], dropna=False)["amount"]
        .sum()
        .reset_index(name="total_spend")
        .sort_values(by="total_spend", ascending=False)
        .head(10)
    )

    full_data["order_date"] = pd.to_datetime(full_data["order_date"], errors="coerce")
    completed["order_date"] = pd.to_datetime(completed["order_date"], errors="coerce")
    latest = full_data["order_date"].max()
    cutoff = latest - pd.Timedelta(days=90) if pd.notna(latest) else pd.NaT

    recent_customer_ids = completed.loc[completed["order_date"] >= cutoff, "customer_id"]
    top_customers["churned"] = ~top_customers["customer_id"].isin(recent_customer_ids)

    top_customers.to_csv(PROCESSED / "top_customers.csv", index=False)
    print("Analysis complete")


if __name__ == "__main__":
    main()
