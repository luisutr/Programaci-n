import pandas as pd
from uploader_wallapop import subir_wallapop

# Leer CSV
df = pd.read_csv("productos.csv")

for _, row in df.iterrows():
    producto = {
        "titulo": row["titulo"],
        "descripcion": row["descripcion"],
        "precio": row["precio"],
        "categoria": row["categoria"],
        "fotos": row["fotos"]
    }
    subir_wallapop(producto)
