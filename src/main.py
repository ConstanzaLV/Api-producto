from fastapi import FastAPI
from src.api.router import router as api_router
from src import models
from src.db.database import engine, SessionLocal
from sqlalchemy.orm import session

app=FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(api_router)
