from fastapi.testclient import TestClient
from app.main import app
import pytest

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

def test_chat_endpoint_returns_correct_html_structure():
    client = TestClient(app)
    response = client.post("/chat", json={"user_message": "Hello", "selectedModel": "pro"})
    assert response.status_code == 200
    assert 'class="ml-4 p-4 rounded-lg' in response.text

@pytest.mark.parametrize(
    "model_name, expected_class",
    [
        ("pro", "bg-white dark:bg-gray-800"),
        ("flash", "border-l-4 border-cyan-400"),
    ],
)
def test_chat_endpoint_is_theme_aware(model_name, expected_class):
    client = TestClient(app)
    response = client.post("/chat", json={"user_message": "test", "selectedModel": model_name})
    assert expected_class in response.text
