# Gemini CLI Master Instructions: AI Chatbot POC

## 1. Core Protocols (The Constitution)

_This section is mandatory boilerplate for every run._

### 1.1. Environment Setup Protocol

- You MUST use the virtual environment's executables for all `pip` or `python` commands.

### 1.2. Agent Changelog Protocol

- **MANDATORY:** After successfully completing the main task, you MUST append a new entry to the `agent_changelog.md` file in the specified format.

## 2. Project Architecture (The Law of the Land)

_This section is mandatory boilerplate for every run._

- **Mandated Technology Stack:** FastAPI, Pytest
- **Context Files for this Task:** You must be aware of `app/main.py`, `tests/test_main.py`, and `static/index.html`.

## 3. Current Task (The Executive Order)

_This section is specific to the current session._

- **Context & State Analysis:** The test `test_read_main_serves_html` in `tests/test_main.py` is currently failing with an `ImportError` because `app/main.py` is empty.

- **This Session's Objective:** Implement the necessary application code to make the failing test pass.

- **Task Directive:**

  1.  Your sole objective is to make the `pytest` command pass.
  2.  You will need to modify `app/main.py`.
  3.  Implement a FastAPI application that serves the `static/index.html` file at the root URL (`/`).
  4.  You have permission to use any appropriate FastAPI method to achieve this (e.g., `FileResponse`, `HTMLResponse`, mounting a static directory, etc.). The choice of implementation is yours, as long as the test passes.

- **Verification Protocol (Definition of Done):**
  - The task is only successfully completed when running `pytest` results in **1 passed**.
