from fastapi.testclient import TestClient
from main import app

# test that the FastAPI app responds correctly
client = TestClient(app)

def test_root():
    response = client.get("/")

    assert response.status_code == 200