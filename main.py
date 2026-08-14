from fastapi import FastAPI
from app import get_system_info
import os
import psycopg2

# FastAPI app object
app = FastAPI(title="System Monitor API") 

@app.get("/")
def root():
    return {
        "message": "System Monitor API is running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "environment": os.getenv("APP_ENV", "unknown")
        }

@app.get("/status")
def status():
    info = get_system_info()

    return {
        "status": info["overall_status"],
        "timestamp": info["timestamp"]
    }

@app.get("/metrics")
def metrics():
    info = get_system_info()

    return {
        "cpu": {
            "usage": info["cpu_usage"],
            "status": info["cpu_status"]
        },
        "memory": {
            "usage": info["memory_usage"],
            "status": info["memory_status"]
        },
        "disk": {
            "usage": info["disk_usage"],
            "status": info["disk_status"]
        }
    }

@app.get("/db-test")
def database_test():
    try:
        connection = get_database_connection()
        connection.close()
        return {"database": "connected"}
    except Exception as e:
        return {"database": "error", "message": str(e)}

    

#DATABASE_HOST = db; db is the PostgreSQL Compose service name.
def get_database_connection():
    return psycopg2.connect(
        host=os.getenv("DATABASE_HOST"),
        port=os.getenv("DATABASE_PORT"),
        database=os.getenv("DATABASE_NAME"),
        user=os.getenv("DATABASE_USER"),
        password=os.getenv("DATABASE_PASSWORD")
    )


