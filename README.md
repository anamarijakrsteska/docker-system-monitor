# System Monitor API

A Python-based system monitoring application that collects CPU, memory, and disk usage, evaluates system health, and exposes the information through a FastAPI REST API. The application is containerized with Docker and uses Docker Compose with PostgreSQL.

## Features

* CPU, memory, and disk monitoring
* Health status classification: `OK`, `WARNING`, `CRITICAL`
* Overall system health status
* FastAPI REST API
* JSON responses
* Interactive API documentation
* Docker containerization
* Docker Compose multi-container setup
* PostgreSQL database
* Persistent PostgreSQL storage with Docker volumes
* Database health checks
* API-to-database communication

## Technologies

* Python
* FastAPI
* Uvicorn
* psutil
* PostgreSQL
* Docker
* Docker Compose

## API Endpoints

| Endpoint       | Description                            |
| -------------- | -------------------------------------- |
| `GET /`        | API status                             |
| `GET /health`  | Complete system information            |
| `GET /status`  | Overall system health                  |
| `GET /metrics` | CPU, memory, and disk metrics          |
| `GET /db-test` | Tests the API-to-PostgreSQL connection |
| `GET /docs`    | Interactive API documentation          |

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the API:

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## Run with Docker Compose

Build and start the containers:

```bash
docker compose up --build
```

The application runs as two containers:

```text
FastAPI API
     ↓
PostgreSQL
```

Check the running services:

```bash
docker compose ps
```

Stop the application:

```bash
docker compose down
```

PostgreSQL data is stored in a persistent Docker volume, so removing the containers does not remove the database data.

## Project Structure

```text
docker-system-monitor/
├── app.py
├── main.py
├── requirements.txt
├── Dockerfile
├── compose.yaml
├── .dockerignore
├── .gitignore
└── README.md
```

## DevOps Concepts Demonstrated

* Docker image creation
* Docker containers
* Port mapping
* Environment variables
* Docker Compose
* Multi-container applications
* Container networking
* PostgreSQL containerization
* Persistent volumes
* Container health checks
* API-to-database communication

## Future Development

* Automated testing
* CI/CD with GitHub Actions
* Docker image registry
* Cloud deployment with AWS
* Infrastructure as Code with Terraform
* Monitoring and observability
* DevSecOps
* Frontend container
