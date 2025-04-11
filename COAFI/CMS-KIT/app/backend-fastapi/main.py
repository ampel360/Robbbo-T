#!/usr/bin/env python3
"""
Main entry point for COAFI FastAPI backend.
Initializes routers, middleware, and memory services.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Import your custom routers
from routers.services import semantic_bridge  # <-- asegúrate que semantic_bridge.py tiene router = APIRouter()
from routers import review  # Import the new review router

app = FastAPI(
    title="COAFI Quantum Memory API",
    description="API para operaciones de memoria semántica, integración con vectores y dashboard",
    version="0.1.0"
)

# Enable CORS for local development / UI frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia esto en prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount routers
app.include_router(semantic_bridge.router, prefix="/semantic-query", tags=["Semantic Query"])
app.include_router(review.router, prefix="/review", tags=["Year-End Review"])  # Include the new review router

# Health check route
@app.get("/")
def read_root():
    return {"status": "COAFI API running", "docs": "/docs", "semantic": "/semantic-query"}

# Entry point
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
