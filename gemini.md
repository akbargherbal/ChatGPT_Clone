# Gemini CLI Master Instructions: AI Chatbot MVP

## 1. Core Protocols (The Constitution)

_This section contains the permanent rules for the agent's behavior across all sessions._

### 1.1. Environment Setup Protocol

- You MUST check for a `.venv` directory. If it does not exist, you MUST create it by running `python -m venv .venv`.
- You MUST use the virtual environment's executables for all `pip` or `python` commands.

### 1.2. Agent Changelog Protocol

- **MANDATORY:** After successfully completing the main task, if it does not exist, create a file named `agent_changelog.md`. You MUST then append a new entry to this file.
- The entry must be in Markdown and follow this exact format:
  ### YYYY-MM-DD HH:MM
  - **What:** [A brief, one-sentence description of the change.]
  - **Why:** [A brief justification for why the change was necessary.]
  - **Files Touched:** [`file1.py`, `file2.html`]

## 2. Project Architecture (The Law of the Land)

_This section defines the non-negotiable technical and structural rules for this specific project._

- **Mandated Technology Stack:** FastAPI, HTMX, Alpine.js, Tailwind CSS.
- **Architectural Constraints:** The backend (`main.py`) must only handle data and logic. It should not contain frontend-specific layout or styling information. The backend is considered complete and correct, verified by the tests in `tests/test_main.py`.

## 3. Current Task (The Executive Order)

_This section is specific to the current session._

- **Context & State Analysis:** The application is currently non-functional.

  1.  **Critical Bug:** Submitting a chat message from the UI results in a `Response Status Error Code 422 from /chat` in the browser console. This is caused by a data mismatch between the HTML form's `name` attributes in `static_mockup.html` and the keys expected by the `ChatRequest` Pydantic model in `main.py`.
  2.  **Enhancement Required:** The `get_gemini_response` function in `main.py` is using outdated Google AI model names.

- **This Session's Objective:** Resolve both the critical bug and the model name issue to make the application fully functional as per Release 0.1.0, and then log the changes.

- **Task Directive:**
  - **Your primary task is to fix the `422` error.** You must modify `static_mockup.html` and/or `main.py` to ensure the data sent from the frontend form correctly matches the structure expected by the backend.
  - **Your secondary task is to update the model names.** In `main.py`, you must change the model strings to use the latest production versions: `gemini-2.5-pro` and `gemini-2.5-flash`.
  - The final implementation must result in a working chat application where a user can send a message and receive a response.
  - The test suite in `tests/test_main.py` MUST pass after your changes.
  - Finally, you MUST create and/or update the `agent_changelog.md` file with a summary of the changes you made, as per the protocol.
