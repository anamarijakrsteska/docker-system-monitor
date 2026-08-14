# System Monitor API

A Python-based system monitoring application that collects CPU, memory, and disk usage, evaluates system health, and exposes the information through a FastAPI REST API.

## Features

* CPU, memory, and disk monitoring
* Health status classification: `OK`, `WARNING`, `CRITICAL`
* Overall system health status
* REST API with FastAPI
* JSON responses
* Interactive API documentation

## Technologies

* Python
* FastAPI
* Uvicorn
* psutil

## API Endpoints

| Endpoint       | Description                   |
| -------------- | ----------------------------- |
| `GET /`        | API status                    |
| `GET /health`  | Complete system information   |
| `GET /status`  | Overall system health         |
| `GET /metrics` | CPU, memory, and disk metrics |
| `GET /docs`    | Interactive API documentation |

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the API:

```bash
uvicorn main:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs <!-- only your PC can access it -->
```

## Project Structure

```text
docker-system-monitor/
├── app.py
├── main.py
├── requirements.txt
└── README.md
```

## Future Development

* Docker containerization
* Docker Compose
* PostgreSQL
* Automated testing
* CI/CD with GitHub Actions
* Cloud deployment




