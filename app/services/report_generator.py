import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from sqlalchemy.orm import Session
from app.models.transaccion import Transaccion

def generar_reporte(db: Session) -> dict:
    # Obtener todas las transacciones
    transacciones = db.query(Transaccion).all()
    if not transacciones:
        return {"grafica_categorias": "", "grafica_mensual": "", "total": 0}

    # Convertir a DataFrame para análisis
    df = pd.DataFrame([{
        "fecha": t.fecha,
        "descripcion": t.descripcion,
        "monto": t.monto,
        "categoria": t.categoria
    } for t in transacciones])

    # Gráfica 1 — Pie chart por categoría
    resumen = df.groupby("categoria")["monto"].sum().reset_index()
    fig_categorias = px.pie(
        resumen,
        values="monto",
        names="categoria",
        title="Gastos por categoría"
    )
    grafica_categorias = fig_categorias.to_html(full_html=False, include_plotlyjs="cdn")

    # Gráfica 2 — Barras por mes
    df["mes"] = pd.to_datetime(df["fecha"]).dt.to_period("M").astype(str)
    mensual = df.groupby("mes")["monto"].sum().reset_index()
    fig_mensual = px.bar(
        mensual,
        x="mes",
        y="monto",
        title="Gastos por mes",
        labels={"mes": "Mes", "monto": "Total ($)"}
    )
    grafica_mensual = fig_mensual.to_html(full_html=False, include_plotlyjs=False)

    return {
        "grafica_categorias": grafica_categorias,
        "grafica_mensual": grafica_mensual,
        "total": round(df["monto"].sum(), 2),
        "cantidad": len(df)
    }