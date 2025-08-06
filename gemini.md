# Gemini CLI Master Instructions: AI Chatbot MVP

## 1. Mandated Technology Stack

The agent MUST use the following technologies exclusively:

- **Backend:** Python with **FastAPI**.
- **Frontend Interaction:** **HTMX**.
- **Client-Side Scripting:** **Alpine.js** (for minimal UI state only).
- **Styling:** **Tailwind CSS**.

## 2. Guiding Constraints

- **Simplicity:** Code must be direct and avoid unnecessary complexity.
- **Stateless Backend:** The FastAPI application should be stateless. State is managed client-side in the browser.
- **HTMX-Driven:** All core chat interactions (sending/receiving messages) MUST be handled via HTMX requests that return HTML fragments.

## 3. Release 0.1.0: Implementation & Verification

The goal is to implement a fully functional backend for the provided `static_mockup.html`.

### 3.1. Required Features:

- **FastAPI Endpoint (`/chat`):**
  - Must accept a `POST` request.
  - Must expect a JSON body containing: `message: str`, `api_key: str`, and `model: str` (either "pro" or "flash").
  - Must return an HTML fragment representing the AI's response message bubble.
- **API Key Persistence:**
  - The application logic (managed by Alpine.js) must save the Google AI API key to the browser's `localStorage` when entered.
  - It must load the API key from `localStorage` on page load, if it exists.
- **Chat Functionality:**
  - The main textarea's input must be sent to the backend via an HTMX `POST` request.
  - The HTML response from the server must be correctly appended to the chat display area.

### 3.2. Verification Protocol (Tests):

The implementation is only considered complete when the following tests pass.

- **Backend Unit Tests:**
  - A test that verifies the `/chat` endpoint returns a `200 OK` status and a valid HTML fragment when given a valid request and a mocked successful API call.
  - A test that verifies the endpoint returns an appropriate HTTP error (e.g., `400 Bad Request`) if `message` or `api_key` is missing from the request.
  - A test that simulates a failure from the external Google AI API and ensures the endpoint handles the error gracefully (e.g., returns an error message HTML fragment).
