# Jenkins Python Demo

A tiny Flask app + tests to learn Jenkins Pipelines.

## Run locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
pytest -q
flask --app app run
```

Visit http://127.0.0.1:5000/health
