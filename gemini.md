# Gemini CLI Master Instructions: AI Chatbot POC

## 1. Core Protocols (The Constitution)

### 1.1. Environment Setup Protocol

- You MUST ensure all dependencies from `requirements.txt` are installed in the `.venv` before running any tests.

### 1.2. Agent Changelog Protocol

- **MANDATORY:** After successfully completing the main task, you MUST append a new entry to the `agent_changelog.md` file in the specified format.

## 2. Project Architecture (The Law of the Land)

- **Mandated Technology Stack:** FastAPI, Pytest, HTMX
- **Context Files for this Task:** You must be aware of the following files: `app/main.py` (which is currently empty) and `tests/test_main.py` (also empty).

## 3. Current Task (The Executive Order)

- **Context & State Analysis:** The project has a complete, version-controlled file structure. All Python files in `app/` are empty. The goal is to begin implementing the first feature using a strict Test-Driven Development (TDD) approach.

- **This Session's Objective:** Write the first failing test case. This test will define the requirements for our root endpoint, which must serve the main HTML file.

- **Task Directive:**

  1.  You are to modify **only one file**: `tests/test_main.py`.
  2.  Add a test function named `test_read_main_serves_html`.
  3.  Inside this test, you will need to:
      - Import the `TestClient`.
      - Instantiate the `TestClient` with a (currently non-existent) `app` object from `app.main`.
      - Use the client to make a `GET` request to the root URL (`/`).
      - Assert that the response has a status code of `200`.
      - Assert that the response HTML content contains the exact string `<title>AI Assistant Chatbot - Final Mockup</title>`.

- **Verification Protocol (Definition of Done):**
  - The task is considered complete once the `tests/test_main.py` file contains the specified test code.
  - **Do not** implement the logic in `app/main.py` to make the test pass. The explicit goal of this session is to create a test that fails correctly. Running `pytest` after your work should result in a `FAILED` status.
