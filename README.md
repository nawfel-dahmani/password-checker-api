# Password Strength Checker API

A cybersecurity REST API built with FastAPI that evaluates password strength and generates secure passwords.

## Features
- Check password strength with a score (0–5) and actionable feedback
- Generate cryptographically random strong passwords
- Rate limiting to prevent abuse (10 req/min on check, 5 req/min on generate)
- Auto-generated interactive docs via Swagger UI

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/check` | Analyze a password |
| GET | `/generate` | Generate a strong password |
| GET | `/health` | Health check |

## Run Locally
```bash
git clone https://github.com/nawfel-dahmani/password-checker-api
cd password-checker-api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open http://127.0.0.1:8000/docs

## Tech Stack
- Python
- FastAPI
- Pydantic
- SlowAPI (rate limiting)