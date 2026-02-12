"""
Valentine's Day Webapp 💕
Run with: uv run app.py
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index():
    return (Path(__file__).parent / "static" / "index.html").read_text()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
