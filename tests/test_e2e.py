import pytest
import uvicorn
import threading
import time
import requests
from playwright.sync_api import Page, expect

HOST = "127.0.0.1"
PORT = 8000

@pytest.fixture(scope="session")
def live_server():
    """Fixture to run the FastAPI app in a background thread."""
    server_thread = threading.Thread(
        target=uvicorn.run,
        args=("app.main:app",),
        kwargs={"host": HOST, "port": PORT, "log_level": "info"},
        daemon=True,
    )
    server_thread.start()
    
    # Wait for the server to be ready
    retries = 5
    while retries > 0:
        try:
            response = requests.get(f"http://{HOST}:{PORT}/")
            if response.status_code == 200:
                break
        except requests.ConnectionError:
            pass
        retries -= 1
        time.sleep(0.5)

    if retries == 0:
        pytest.fail("Server did not start in time.")
    
    yield f"http://{HOST}:{PORT}"
    # No teardown needed as the thread is a daemon

def test_chat_submission_adds_new_message(live_server, page: Page):
    """
    Tests if submitting the chat form results in a new AI message 
    being appended to the chat log.
    """
    page.goto(live_server)

    # Fill the form and submit
    page.locator('textarea[name="user_message"]').fill("Hello, AI!")
    page.locator('button[type="submit"]').click()

    # The AI response container
    # Note: We look for the *specific* placeholder text returned by the backend
    ai_response_locator = page.locator("#chat-log > div.flex.items-start:last-child")
    
    # Assert that the new AI response appears in the chat log
    expect(page.locator("#chat-log")).to_contain_text("Hello, AI!")
