# src/backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import data

app = FastAPI(
    title="Education Access Insights API",
    description="Backend API for the Education Access Insights Dashboard",
    version="0.1.0",
)

# Allow frontend (Streamlit) to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: tighten this later if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(data.router, prefix="/data", tags=["data"])


@app.get("/", summary="Health check")
def read_root():
    return {"message": "Education Access Insights API is running"}
