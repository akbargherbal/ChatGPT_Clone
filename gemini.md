# Gemini CLI Master Instructions: AI Chatbot POC

## 1. Core Protocols (The Constitution)

_This section is mandatory boilerplate for every run._

### 1.1. Environment Setup Protocol

- You MUST check for a `.venv` directory. If it does not exist, you MUST create it by running `python -m venv .venv`.
- You MUST use the virtual environment's executables for all `pip` or `python` commands.

### 1.2. Agent Changelog Protocol

- **MANDATORY:** After successfully completing the main task, you MUST append a new entry to the `agent_changelog.md` file in the following format:
  ```markdown
  ### YYYY-MM-DD HH:MM

  - **What:** [A brief, one-sentence description of the change.]
  - **Why:** [A brief justification for why the change was necessary.]
  - **Files Touched:** [`file1.py`, `file2.html`]
  ```

## 2. Project Architecture (The Law of the Land)

_This section is mandatory boilerplate for every run._

- **Mandated Technology Stack:** FastAPI, Pytest
- **Context Files for this Task:** You must be aware of the contents of `tests/test_main.py` and `app/main.py`.

## 3. Current Task (The Executive Order)

_This is the only section that changes significantly between runs._

- **Context & State Analysis:** The test suite currently has one passing test, `test_read_main_serves_html`, which confirms the root endpoint (`/`) works correctly. There is no endpoint for `/chat`.

- **This Session's Objective:** Create a new, failing test case to drive the development of the `/chat` endpoint.

- **Task Directive:**

  1. Your sole objective is to add a new test function to the `tests/test_main.py` file.
  2. The new test function must be named `test_chat_endpoint_returns_success`.
  3. Inside this new test, use the `TestClient` to send a `POST` request to the `/chat` endpoint.
  4. The `POST` request should include a simple JSON payload: `{"user_message": "Hello", "selectedModel": "pro"}`.
  5. The test must assert that the response has a status code of `200`.
  6. **Do not modify `app/main.py`**. The purpose of this task is only to create the failing test.

- **Verification Protocol (Definition of Done):**
  - The task is successfully completed when running `pytest` results in **1 passed and 1 failed**. The new test, `test_chat_endpoint_returns_success`, is expected to fail with a `404 Not Found` error.
