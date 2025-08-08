from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
import os
from app.models import ChatRequest
from app.templates import create_ai_message
from fastapi import Form

app = FastAPI()


@app.get("/")
async def read_index():
    # Construct the absolute path to the index.html file
    static_dir = os.path.join(os.path.dirname(__file__), "..", "static")
    index_path = os.path.join(static_dir, "index.html")
    return FileResponse(index_path)


@app.post("/chat")
async def chat(user_message: str = Form(...), selectedModel: str = Form(...)):
    # Using the new template function to generate the response
    ai_message_html = create_ai_message(user_message, selectedModel)
    return HTMLResponse(content=ai_message_html)
