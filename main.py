# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.facebook import router as facebook_router
from routes.token import router as token_router

app = FastAPI(title="Facebook Image Post API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(facebook_router)
app.include_router(token_router)

@app.get("/")
def home():
    return {"message": "Facebook Image Post API is running! 🚀"}