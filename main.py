from fastapi import FastAPI
import pandas as pd
import numpy as np

app = FastAPI(title='Proyecto Individual',
            description='Autor:  Atencio Marcelo',
            version='1.0.1')


@app.get("/genero/{x}",tags=["Género"])
def PlayTimeGenre(x: str):

    # Cargar el archivo CSV en un DataFrame
    df = pd.read_csv("../ETL/03 - Dataframe para funciones/PlayTimeGenre.csv")

    # Filtrar el DataFrame para el género específico
    df_genero = df.loc[df['Genero'] == x]

    # Encontrar el año con más horas jugadas para ese género
    año_max_playtime = df_genero.loc[df_genero['playtime_forever'].idxmax(), 'Año_Lanzamiento']

    # Crear la leyenda
    leyenda = f"Año de lanzamiento con más horas jugadas para Género {x}: {año_max_playtime}"

    return {"Respuesta" : leyenda}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)