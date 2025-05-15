from fastapi import FastAPI
from src.api.router import router as api_router
from src import models
from src.db.database import engine, SessionLocal
from sqlalchemy.orm import session
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

models.Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    # puedes añadir más si lo necesitas
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # o ["*"] para permitir todos en desarrollo
    allow_credentials=True,
    allow_methods=["*"],              # GET, POST, PUT, DELETE…
    allow_headers=["*"],              # Content-Type, Authorization…
)

app.include_router(api_router)
