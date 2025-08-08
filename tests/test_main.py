from fastapi.testclient import TestClient
from app.main import app

def test_read_main_serves_html():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert "<title>AI Assistant Chatbot - Final Mockup</title>" in response.text
