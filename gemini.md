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

- **Context & State Analysis:** The test `test_chat_endpoint_returns_success` is failing because it asserts a `Content-Type` of `text/html; charset=utf-8`, but the endpoint is currently returning `application/json`.

- **This Session's Objective:** Modify the `/chat` endpoint to return an HTML response, making the test suite pass.

- **Task Directive:**

  1.  Your sole objective is to make the `pytest` command pass with **2 passed**.
  2.  You will need to modify the `chat` function in `app/main.py`.
  3.  You must import `HTMLResponse` from `fastapi.responses`.
  4.  Change the endpoint's return statement to use `HTMLResponse`.
  5.  For now, the content can be a simple, non-empty HTML string. For example: `return HTMLResponse(content="<div>Response</div>")`.

- **Verification Protocol (Definition of Done):**
  - The task is successfully completed only when running `pytest` results in **2 passed**.
