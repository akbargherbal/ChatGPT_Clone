# Gemini CLI Master Instructions: AI Chatbot POC

## 1. Core Protocols (The Constitution)

_This section is mandatory boilerplate for every run._

### 1.1. Environment Setup Protocol

- You MUST check for a `.venv` directory. If it does not exist, you MUST create it by running `python -m venv .venv`.
- You MUST use the virtual environment's executables for all `pip` or `python` commands.

## 2. Project Architecture (The Law of the Land)

_This section is mandatory boilerplate for every run._

- **Mandated Technology Stack:** FastAPI, Pytest, Pydantic
- **Context Files for this Task:** You must be aware of `tests/test_main.py` and `app/main.py`.

## 3. Current Task (The Executive Order)

_This section is specific to the current session._

- **Context & State Analysis:** All tests are currently passing. The `/chat` endpoint successfully returns a response with a `Content-Type` of `text/html; charset=utf-8`. However, the test does not verify the actual content of the HTML.

- **This Session's Objective:** Modify the chat endpoint test to verify that the returned HTML contains structured content, creating a new failing test.

- **Task Directive:**

  1.  Your sole objective is to modify the test named `test_chat_endpoint_returns_success` in `tests/test_main.py`.
  2.  Add a new assertion to the test. This assertion must verify that the response body (i.e., `response.text`) contains the HTML tag `<p>`.
  3.  **Do not modify `app/main.py`**. The purpose is only to update the test to make it fail.

- **Verification Protocol (Definition of Done):**
  - The task is successfully completed when running `pytest` results in **1 passed and 1 failed**.
