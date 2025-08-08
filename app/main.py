from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
import os
from app.models import ChatRequest

app = FastAPI()

@app.get("/")
async def read_index():
    # Construct the absolute path to the index.html file
    static_dir = os.path.join(os.path.dirname(__file__), '..', 'static')
    index_path = os.path.join(static_dir, 'index.html')
    return FileResponse(index_path)

@app.post("/chat")
async def chat(chat_request: ChatRequest):
    return HTMLResponse(content="<div>Response</div>")
