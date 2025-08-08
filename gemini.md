# Gemini CLI Master Instructions: AI Chatbot POC

## 1. Core Protocols (The Constitution)

_This section is mandatory boilerplate for every run._

### 1.1. Environment Setup Protocol

- You MUST check for a `.venv` directory. If it does not exist, you MUST create it by running `python -m venv .venv`.
- You MUST use the virtual environment's executables for all `pip` or `python` commands.

## 2. Project Architecture (The Law of the Land)

_This section is mandatory boilerplate for every run._

- **Mandated Technology Stack:** FastAPI, Pytest, Pydantic
- **Context Files for this Task:** You must be aware of the contents of `agent_changelog.md`.

## 3. Current Task (The Executive Order)

_This section is specific to the current session._

- **Context & State Analysis:** The application code has been successfully modified to return HTML containing a `<p>` tag from the `/chat` endpoint. This change has been tested and committed. The `agent_changelog.md` file now needs to be updated to reflect this change.

- **This Session's Objective:** Append a new entry to the changelog.

- **Task Directive:**

  1.  Your sole objective is to append a new entry to the end of the `agent_changelog.md` file.
  2.  The entry to add is:
      ```markdown
      ### 2025-08-08 12:15

      - **What:** Modified the /chat endpoint to return HTML containing a `<p>` tag.
      - **Why:** To satisfy the test requirement for structured HTML content.
      - **Files Touched:** [`app/main.py`, `tests/test_main.py`]
      ```
  3.  **Do not run `pytest`.**

- **Verification Protocol (Definition of Done):**
  - The task is successfully completed when the specified entry has been appended to `agent_changelog.md`.
