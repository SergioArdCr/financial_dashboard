from sqlalchemy import Column, Integer, String, Float, Date
from app.db.database import Base

class Transaccion(Base):
    __tablename__ = "transacciones"
    id          = Column(Integer, primary_key=True, autoincrement=True)
    fecha       = Column(Date)
    descripcion = Column(String)
    monto       = Column(Float)
    categoria   = Column(String)