# Data Pipeline Dashboard

Built an end-to-end data pipeline and analytics platform that processes raw transactional data, generates business insights, and exposes them through APIs and an interactive dashboard.

Designed with a focus on data reliability, modular architecture, and real-world usability.

## What It Includes

- raw CSV datasets for customers, orders, and products
- a cleaning pipeline for standardization and validation
- an analysis layer that produces revenue and customer insight reports
- a FastAPI backend exposing analytics endpoints
- a frontend dashboard with charts and customer summaries

## Project Structure

```text
.
├── analyze.py
├── backend/
│   └── main.py
├── clean_data.py
├── data/
│   ├── processed/
│   └── raw/
├── frontend/
│   └── index.html
└── README.md
```

## Run

Install the Python dependencies first:

```bash
pip install pandas fastapi uvicorn
```

Run the pipeline:

```bash
python clean_data.py
python analyze.py
```

Start the API from the repository root:

```bash
uvicorn backend.main:app --reload
```

Open [frontend/index.html](/home/jet/Desktop/dpd/frontend/index.html) in a browser after the backend is running.

## Outputs

The pipeline generates:

- [customers_clean.csv](/home/jet/Desktop/dpd/data/processed/customers_clean.csv)
- [orders_clean.csv](/home/jet/Desktop/dpd/data/processed/orders_clean.csv)
- [monthly_revenue.csv](/home/jet/Desktop/dpd/data/processed/monthly_revenue.csv)
- [category_revenue.csv](/home/jet/Desktop/dpd/data/processed/category_revenue.csv)
- [regional_revenue.csv](/home/jet/Desktop/dpd/data/processed/regional_revenue.csv)
- [top_customers.csv](/home/jet/Desktop/dpd/data/processed/top_customers.csv)
