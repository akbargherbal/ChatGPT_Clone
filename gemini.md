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
- **Context Files for this Task:** You must be aware of `tests/test_main.py`, `app/main.py`, and `app/models.py`.

## 3. Current Task (The Executive Order)

_This section is specific to the current session._

- **Context & State Analysis:** The test `test_chat_endpoint_returns_success` is failing with a `404 Not Found` error. Our goal is to make this test pass.

- **This Session's Objective:** Implement the `/chat` endpoint and the necessary data model to make the failing test pass.

- **Task Directive:**
  1.  Your primary objective is to make the `pytest` command result in **2 passed**.
  2.  **In `app/models.py`**, define a Pydantic model named `ChatRequest`. It must have two fields: `user_message` (a string) and `selectedModel` (a string). You will need to import `BaseModel` from `pydantic`.
  3.  **In `app/main.py`**, you must implement a new endpoint to make the test pass.
  4.  The endpoint must respond to `POST /chat`.
  5.  The function signature must accept the `ChatRequest` model as its body.
  6.  The endpoint should return a simple JSON response with a status of 200. Example: `{"status": "ok"}`.
  7.  You will need to import the `ChatRequest` model in `app/main.py`.

- **Verification Protocol (Definition of Done):**
  - The task is only successfully completed when running `pytest` results in **2 passed**.


