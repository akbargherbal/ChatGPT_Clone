import os
import google.generativeai as genai
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()


class ChatRequest(BaseModel):
    message: str
    api_key: str
    model: str


app = FastAPI()


def get_gemini_response(message: str, api_key: str, model: str):
    try:
        genai.configure(api_key=api_key)
        model_name = "gemini-pro" if model == "pro" else "gemini-1.5-flash-latest"
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(message)
        return response.text
    except Exception as e:
        raise e


@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        response_text = get_gemini_response(request.message, request.api_key, request.model)
        return HTMLResponse(content=f'<div class="message ai-message">{response_text}</div>')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'<div class="message error-message">Error: {e}</div>')