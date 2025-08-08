# Gemini CLI Master Instructions: AI Chatbot POC

## 1. Core Protocols (The Constitution)

_This section is mandatory boilerplate for every run._

### 1.1. Environment Setup Protocol

- You MUST check for a `.venv` directory. If it does not exist, you MUST create it by running `python -m venv .venv`.
- You MUST use the virtual environment's executables for all `pip` or `python` commands.

### 1.2. Agent Changelog Protocol

- **REMOVED FOR THIS RUN:** This is a "Code Run" as per our Decoupled Mandate Protocol. The changelog will be updated in a separate, subsequent "Logging Run".

## 2. Project Architecture (The Law of the Land)

_This section is mandatory boilerplate for every run._

- **Mandated Technology Stack:** FastAPI, Pytest, Pydantic
- **Architectural Constraints:** The generation of HTML snippets for API responses MUST be handled by functions within the `app/templates.py` file. The `app/main.py` file should import and call these functions.
- **Context Files for this Task:** You must be aware of the contents of `app/main.py`, `tests/test_main.py`, and the new requirement to create `app/templates.py`.

## 3. Current Task (The Executive Order)

_This section is specific to the current session._

- **Context & State Analysis:** A new test, `test_chat_endpoint_returns_correct_html_structure`, is failing because the response from the `/chat` endpoint does not contain the required HTML structure (`<div class="prose...`). The current implementation returns a hard-coded, simple HTML string.

- **This Session's Objective:** Implement the necessary code to make the failing test `test_chat_endpoint_returns_correct_html_structure` pass.

- **Task Directive:**
  1.  Create a new file named `app/templates.py`.
  2.  Inside `app/templates.py`, create a new function named `create_ai_message`. This function should accept a single string argument `message_text`.
  3.  The `create_ai_message` function must return an HTML string with the following structure, using the `message_text` as the content of the `<p>` tag:
      ```html
      <div class="ml-4 p-4 rounded-lg max-w-lg prose prose-sm dark:prose-invert transition-all bg-white dark:bg-gray-800">
          <p>[MESSAGE_TEXT_GOES_HERE]</p>
      </div>
      ```
  4.  In `app/main.py`, import the `create_ai_message` function from `app.templates`.
  5.  Modify the `/chat` endpoint in `app/main.py`. It should now call `create_ai_message`, passing some placeholder text to it, and return the resulting HTML in the `HTMLResponse`.

- **Verification Protocol (Definition of Done):**
  - The task is successfully completed when running `pytest` results in **3 passed** tests.