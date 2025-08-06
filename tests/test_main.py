import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from main import app

client = TestClient(app)


# This test now correctly patches the 'GenerativeModel' from the google library
def test_chat_success():
    with patch("google.generativeai.GenerativeModel") as mock_model:
        # This simulates the response object from the Google AI library
        mock_response = MagicMock()
        mock_response.text = "Mock AI Response"
        mock_model.return_value.generate_content.return_value = mock_response

        response = client.post(
            "/chat", json={"message": "Hello", "api_key": "test_key", "model": "pro"}
        )
        assert response.status_code == 200
        # We expect the final implementation to return an HTML fragment
        assert '<div class="message ai-message">Mock AI Response</div>' in response.text


def test_chat_missing_message():
    response = client.post("/chat", json={"api_key": "test_key", "model": "pro"})
    assert response.status_code == 422


def test_chat_missing_api_key():
    response = client.post("/chat", json={"message": "Hello", "model": "pro"})
    assert response.status_code == 422


# This test also correctly patches the actual library call
def test_chat_google_api_failure():
    with patch("google.generativeai.GenerativeModel") as mock_model:
        # This simulates the library raising an error
        mock_model.return_value.generate_content.side_effect = Exception(
            "Google AI Error"
        )

        response = client.post(
            "/chat", json={"message": "Hello", "api_key": "test_key", "model": "pro"}
        )
        assert response.json()["detail"] == '<div class="message error-message">Error: Google AI Error</div>'
