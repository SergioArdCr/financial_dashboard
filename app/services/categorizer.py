REGLAS = {
    "Alimentación":    ["restaurante", "mcdonald", "burger", "pizza", "supermercado", "exito", "carulla", "rappi", "domicilio"],
    "Transporte":      ["uber", "taxi", "cabify", "gasolina", "peaje", "transmilenio", "sitp"],
    "Entretenimiento": ["netflix", "spotify", "steam", "cinema", "cine", "disney", "youtube"],
    "Salud":           ["farmacia", "drogueria", "medico", "clinica", "hospital", "gym", "gimnasio"],
    "Servicios":       ["energia", "agua", "gas", "internet", "telefono", "claro", "movistar", "tigo"],
    "Educacion":       ["universidad", "curso", "udemy", "libro", "libreria"],
    "Ropa":            ["zara", "h&m", "adidas", "nike", "falabella", "studio f"],
}

def categorizar(descripcion: str) -> str:
    descripcion_lower = descripcion.lower()
    for categoria, palabras in REGLAS.items():
        if any(palabra in descripcion_lower for palabra in palabras):
            return categoria
    return "Otros"