from fastapi import FastAPI
from datetime import datetime
import os

app = FastAPI(title="DevOps Docker CI/CD Lab", version="1.0.0")

@app.get("/")
def home():
    return {
        "message": "DevOps Docker CI/CD Lab is running",
        "environment": os.getenv("APP_ENV", "local"),
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/version")
def version():
    return {
        "app": "devops-docker-cicd-lab",
        "version": "1.0.0"
    }
