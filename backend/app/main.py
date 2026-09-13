from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.api.predictions import router as predictions_router

app = FastAPI(
    title="MoneyTalks",
    description="Backend API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(predictions_router)

@app.get("/")
def root():
    return { "message": "MoneyTalks API is running" }

@app.get("/health")
def health():
    return { "status": "OK" }