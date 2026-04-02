# Data Pipeline Dashboard

Small end-to-end analytics project with:

- raw CSV datasets
- a cleaning script
- an analysis script
- a FastAPI backend
- a simple frontend dashboard

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
