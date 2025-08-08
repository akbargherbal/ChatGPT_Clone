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

- **Mandated Technology Stack:** FastAPI, Pytest, Playwright
- **Context Files for this Task:** You must be aware of `agent_changelog.md`.

## 3. Current Task (The Executive Order)

- **Context & State Analysis:** The application now correctly echoes the user's message back in the AI response. This has been verified by our test suite and the changes have been committed.
- **This Session's Objective:** Append two new entries to the `agent_changelog.md` to document the TDD cycle for the echo feature.
- **Task Directive:**

1.  Your sole objective is to append two new entries to the end of the `agent_changelog.md` file.
2.  The **first entry** to add is for the test creation:

```markdown
### 2025-08-08 15:00

- **What:** Added a failing test to verify the chat endpoint echoes the user's message.
- **Why:** To drive the implementation of dynamic responses via TDD.
- **Files Touched:** [`tests/test_main.py`]
```

3.  The **second entry** to add is for the implementation:

```markdown
### 2025-08-08 15:05

- **What:** Modified the /chat endpoint to echo the user's input.
- **Why:** To make the echo test pass and confirm the user input is being processed correctly.
- **Files Touched:** [`app/main.py`]
```

4.  **Do not run `pytest`.**

- **Verification Protocol (Definition of Done):**
- The task is successfully completed when the two specified entries have been appended to `agent_changelog.md`.
