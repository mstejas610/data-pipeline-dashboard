# End-to-End Data Analytics Platform

> A compact full-stack analytics system that cleans raw business data, generates reports, exposes them through APIs, and presents them in a browser dashboard.

Built with a focus on data reliability, modular structure, and real-world workflow design. The project simulates a practical analytics pipeline where raw input moves through cleaning, transformation, reporting, API delivery, and visualization.

## Snapshot

| Area | What it does |
| --- | --- |
| Data Cleaning | Standardizes dates, removes duplicate customers, validates emails, normalizes order status, and fills missing values |
| Analysis | Produces monthly revenue, category revenue, regional revenue, and top-customer reports |
| Backend | Serves processed analytics through FastAPI endpoints with basic error handling |
| Frontend | Displays charts and summary views for revenue, categories, regions, and customer activity |

## Architecture

```text
Raw CSV files
    |
    v
clean_data.py
    |
    v
Processed CSV outputs
    |
    v
analyze.py
    |
    v
Analytics reports
    |
    v
FastAPI backend
    |
    v
Frontend dashboard
```

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
├── requirements.txt
└── README.md
```

## Features

- Cleans and standardizes customer and order datasets
- Generates reusable processed CSV outputs
- Produces business-facing analytics reports
- Exposes reports through REST endpoints
- Renders a lightweight dashboard with multiple views

## Quick Start

1. Create and activate a virtual environment.
2. Install dependencies.
3. Run the cleaning and analysis pipeline.
4. Start the backend.
5. Open the frontend dashboard.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python clean_data.py
python analyze.py
uvicorn backend.main:app --reload
```

Open [frontend/index.html](/home/jet/Desktop/dpd/frontend/index.html) in a browser once the API is running.

## API Endpoints

| Endpoint | Purpose |
| --- | --- |
| `/health` | Basic health check |
| `/api/revenue` | Monthly completed-order revenue |
| `/api/top-customers` | Top customers ranked by spend |
| `/api/categories` | Revenue grouped by product category |
| `/api/regions` | Revenue grouped by region |

## Generated Outputs

The pipeline creates these processed and reporting files:

- [customers_clean.csv](/home/jet/Desktop/dpd/data/processed/customers_clean.csv)
- [orders_clean.csv](/home/jet/Desktop/dpd/data/processed/orders_clean.csv)
- [monthly_revenue.csv](/home/jet/Desktop/dpd/data/processed/monthly_revenue.csv)
- [category_revenue.csv](/home/jet/Desktop/dpd/data/processed/category_revenue.csv)
- [regional_revenue.csv](/home/jet/Desktop/dpd/data/processed/regional_revenue.csv)
- [top_customers.csv](/home/jet/Desktop/dpd/data/processed/top_customers.csv)

## Tech Stack

- Python
- pandas
- FastAPI
- Uvicorn
- HTML, CSS, JavaScript
- Chart.js

## Design Notes

- Processed data is stored separately from raw input for repeatable runs.
- The backend resolves file paths from the project root to avoid working-directory issues.
- Revenue calculations are based only on completed orders.
- The frontend includes loading and error states so failures are visible instead of silent.

## Why This Project Exists

This project was designed to simulate a real-world analytics workflow where data flows from raw ingestion to actionable insights through clean pipelines and modular services.
