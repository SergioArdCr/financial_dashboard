from fastapi import FastAPI
from sqlalchemy import engine
from app.db.database import Base, engine
from app.routers import urls

app = FastAPI(title="URL Shortener API")

Base.metadata.create_all(bind=engine)

app.include_router(urls.router)