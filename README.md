# Bike Sharing Analysis (Streamlit)

This repository contains a small Streamlit app (`Main.py`) for analyzing a bike-sharing dataset.

Requirements
- Python 3.8+
- Install dependencies (recommended in a venv):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run locally

```bash
streamlit run Main.py --server.headless true --server.port 8501
# then open http://localhost:8501 in your browser
```

Notes
- The app loads data from a remote CSV. If you want to run fully offline, download the CSV and change `DATA_URL` in `Main.py`.
- If you see a matplotlib warning about tick labels, the app code already sets ticks explicitly to avoid that.
