# -*- coding: utf-8 -*-
"""
Single-Command Runner for Kumaoni Voice Translator.
Runs the FastAPI backend and provides instant web access at http://localhost:8000.
"""

import os
import sys
import subprocess
import webbrowser
from pathlib import Path

# Add project roots to path
CURRENT_DIR = Path(__file__).resolve().parent
BACKEND_DIR = CURRENT_DIR / "backend"
FRONTEND_DIR = CURRENT_DIR / "frontend"
LIB_DIR = CURRENT_DIR.parent

sys.path.insert(0, str(LIB_DIR))
sys.path.insert(0, str(BACKEND_DIR))

try:
    import uvicorn
    from fastapi.staticfiles import StaticFiles
    from backend.server import app
except ImportError:
    print("Installing backend dependencies (fastapi, uvicorn)...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "fastapi", "uvicorn"])
    import uvicorn
    from fastapi.staticfiles import StaticFiles
    from backend.server import app

# Mount static frontend directory directly for standalone execution
if FRONTEND_DIR.exists():
    app.mount("/src", StaticFiles(directory=str(FRONTEND_DIR / "src")), name="src")
    
    @app.get("/")
    def serve_index():
        from fastapi.responses import FileResponse
        return FileResponse(str(FRONTEND_DIR / "index.html"))


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    url = f"http://localhost:{port}"
    print(f"\n=======================================================")
    print(f"🎙️  Kumaoni Voice Translator Web Application")
    print(f"=======================================================")
    print(f"🚀 Running at: {url}")
    print(f"📖 Swagger Docs: {url}/docs")
    print(f"Press CTRL+C to stop.\n")

    try:
        webbrowser.open(url)
    except Exception:
        pass

    uvicorn.run(app, host="127.0.0.1", port=port, log_level="info")


if __name__ == "__main__":
    main()
