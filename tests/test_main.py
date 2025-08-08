from fastapi.testclient import TestClient
from app.main import app

def test_read_main_serves_html():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert "<title>AI Assistant Chatbot - Final Mockup</title>" in response.text

def test_chat_endpoint_returns_success():
    client = TestClient(app)
    response = client.post("/chat", json={"user_message": "Hello", "selectedModel": "pro"})
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert "<p>" in response.text