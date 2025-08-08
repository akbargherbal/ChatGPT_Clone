from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

@app.get("/")
async def read_index():
    # Construct the absolute path to the index.html file
    static_dir = os.path.join(os.path.dirname(__file__), '..', 'static')
    index_path = os.path.join(static_dir, 'index.html')
    return FileResponse(index_path)
