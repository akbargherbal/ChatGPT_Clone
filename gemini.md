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

- **Mandated Technology Stack:** FastAPI, Pytest, Pydantic
- **Context Files for this Task:** You must be aware of `tests/test_main.py` and `app/main.py`.

## 3. Current Task (The Executive Order)

_This section is specific to the current session._

- **Context & State Analysis:** All tests are currently passing. The `/chat` endpoint correctly accepts a POST request and returns a JSON response with a 200 status code. However, the project requirements state this endpoint must return an HTML snippet for HTMX.

- **This Session's Objective:** Modify the existing test `test_chat_endpoint_returns_success` to enforce the requirement that the endpoint returns HTML, thereby creating a new failing test.

- **Task Directive:**

  1.  Your sole objective is to modify the test named `test_chat_endpoint_returns_success` in the `tests/test_main.py` file.
  2.  Add a new assertion to this test.
  3.  The new assertion must check the `Content-Type` header of the response and verify that it is equal to `text/html; charset=utf-8`.
  4.  **Do not modify `app/main.py`**. The purpose is only to update the test file and cause a failure.

- **Verification Protocol (Definition of Done):**
  - The task is successfully completed when running `pytest` results in **1 passed and 1 failed**. The `test_chat_endpoint_returns_success` test is now expected to fail on the new `Content-Type` header assertion.
