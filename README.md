# DevOps Docker CI/CD Lab

## Overview
A real DevOps portfolio project that demonstrates application containerization, automated testing, Docker image building and CI/CD using GitHub Actions.

This project is designed for IT Specialist, System Administrator, Junior DevOps and Infrastructure roles.

## What This Project Demonstrates
- Docker containerization
- Docker Compose
- GitHub Actions CI pipeline
- Automated Python tests
- API health checks
- Basic production-style project structure

## Tech Stack
- Python
- FastAPI
- Docker
- Docker Compose
- GitHub Actions
- Pytest
- Linux-based container runtime

## Project Structure
```text
devops-docker-cicd-lab/
├── app/
│   └── main.py
├── tests/
│   └── test_app.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md
```

## API Endpoints
| Endpoint | Purpose |
|---|---|
| `/` | Main status endpoint |
| `/health` | Health check endpoint |
| `/version` | Application version |

## Run Locally Without Docker
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:
```text
http://localhost:8000
```

## Run With Docker
```bash
docker build -t devops-docker-cicd-lab .
docker run -p 8000:8000 devops-docker-cicd-lab
```

## Run With Docker Compose
```bash
docker compose up --build
```

Open:
```text
http://localhost:8000/health
```

## Run Tests
```bash
pytest -v
```

## CI/CD Pipeline
The GitHub Actions workflow runs automatically on every push or pull request to `main`.

Pipeline steps:
1. Checkout code
2. Install Python
3. Install dependencies
4. Run automated tests
5. Build Docker image
6. Start container and run health check

## Interview Explanation
I built this project to demonstrate a complete DevOps workflow:
- The application is packaged inside a Docker container.
- Tests validate that the API works correctly.
- GitHub Actions automatically tests and builds the project.
- A health check confirms the container is running properly.
- Docker Compose makes it easy to run the service in a local lab environment.

## Author
Tiran Benisti  
Email: tiri18b@gmail.com
