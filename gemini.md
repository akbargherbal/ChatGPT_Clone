# Gemini CLI Master Instructions: AI Chatbot POC

## 1. Core Protocols (The Constitution)

_This section is mandatory boilerplate for every run._

### 1.1. Environment Setup Protocol
- You MUST check for a `.venv` directory. If it does not exist, you MUST create it by running `python -m venv .venv`.
- You MUST use the virtual environment's executables for all `pip` or `python` commands.

### 1.2. Agent Changelog Protocol
- **REMOVED FOR THIS RUN:** This is a "Code Run."

## 2. Project Architecture (The Law of the Land)

_This section is mandatory boilerplate for every run._

- **Mandated Technology Stack:** FastAPI, Pytest, Playwright
- **Context Files for this Task:** You must be aware of the contents of `app/main.py` and `tests/test_main.py`.

## 3. Current Task (The Executive Order)

_This section is specific to the current session._

- **Context & State Analysis:** A new test, `test_chat_endpoint_echoes_user_message`, is failing because the `/chat` endpoint currently ignores the user's input and sends a hard-coded placeholder string to the template function.

- **This Session's Objective:** Implement the necessary logic to make the failing "echo" test pass.

- **Task Directive:**
  1.  Open the file `app/main.py`.
  2.  Locate the `/chat` endpoint function.
  3.  Find the line where `create_ai_message` is called.
  4.  Modify the call to pass the `user_message` variable received from the form as the first argument, instead of the hard-coded string `"This is a placeholder response from the AI."`.

- **Verification Protocol (Definition of Done):**
  - The task is successfully completed when running `pytest` results in **7 passed** tests.