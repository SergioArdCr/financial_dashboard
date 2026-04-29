from pydantic import BaseModel
from datetime import date

class TransaccionResponse(BaseModel):
    id: int
    fecha: date
    descripcion: str
    monto: float
    categoria: str

    class Config:
        from_attributes = True

class ResumenCategoria(BaseModel):
    categoria: str
    total: float
    cantidad: int