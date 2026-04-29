from fastapi import FastAPI
from app.routers import finanzas
from app.db.database import Base, engine
from app.models import transaccion

app = FastAPI(title="Financial Dashboard API")

Base.metadata.create_all(bind=engine)
app.include_router(finanzas.router)