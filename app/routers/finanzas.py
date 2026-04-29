import io
import pandas as pd
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.db.database import get_db
from app.models.transaccion import Transaccion
from app.schemas.transaccion import ResumenCategoria
from app.services.categorizer import categorizar
from app.services.report_generator import generar_reporte
from fastapi.templating import Jinja2Templates
from jinja2 import Environment, FileSystemLoader

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.post("/upload")
def subir_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Solo se aceptan archivos CSV")

    contenido = file.file.read()
    df = pd.read_csv(io.BytesIO(contenido))

    # Verificar columnas requeridas
    columnas = [c.lower() for c in df.columns]
    if not all(c in columnas for c in ["fecha", "descripcion", "monto"]):
        raise HTTPException(status_code=400, detail="El CSV debe tener columnas: fecha, descripcion, monto")

    df.columns = [c.lower() for c in df.columns]
    df["fecha"] = pd.to_datetime(df["fecha"])
    df["monto"] = df["monto"].abs()  # asegura que todos sean positivos

    # Limpiar tabla y recargar
    db.query(Transaccion).delete()

    for _, fila in df.iterrows():
        transaccion = Transaccion(
            fecha=fila["fecha"].date(),
            descripcion=fila["descripcion"],
            monto=fila["monto"],
            categoria=categorizar(fila["descripcion"])
        )
        db.add(transaccion)

    db.commit()
    return {"mensaje": f"{len(df)} transacciones cargadas correctamente"}

@router.get("/reporte", response_class=HTMLResponse)
def ver_reporte(db: Session = Depends(get_db)):
    datos = generar_reporte(db)
    
    env = Environment(loader=FileSystemLoader("app/templates"))
    template = env.get_template("reporte.html")
    html = template.render(**datos)
    
    return HTMLResponse(content=html)

@router.get("/resumen", response_model=list[ResumenCategoria])
def ver_resumen(db: Session = Depends(get_db)):
    resultados = db.query(
        Transaccion.categoria,
        func.sum(Transaccion.monto).label("total"),
        func.count(Transaccion.id).label("cantidad")
    ).group_by(Transaccion.categoria).all()

    return [ResumenCategoria(categoria=r.categoria, total=round(r.total, 2), cantidad=r.cantidad)
            for r in resultados]