from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import pandas as pd
import numpy as np

app = FastAPI(title='Proyecto Individual',
            description='Autor:  Atencio Marcelo')


@app.get("/genero/{x}",tags=["Año de lanzamiento con más horas jugadas según el género"])
def PlayTimeGenre(x: str):

    # Cargar el archivo CSV en un DataFrame
    df = pd.read_csv("ETL/03 - Dataframe para funciones/PlayTimeGenre.csv")

    # Filtrar el DataFrame para el género específico
    df_genero = df.loc[df['Genero'] == x]

    # Encontrar el año con más horas jugadas para ese género
    año_max_playtime = df_genero.loc[df_genero['playtime_forever'].idxmax(), 'Año_Lanzamiento']

    # Crear la leyenda
    leyenda = f"Año de lanzamiento con más horas jugadas para Género {x}: {año_max_playtime}"

    return leyenda

@app.get("/genero_user/{x}",tags=["Usuario con más horas jugadas según el género"])
def UserForGenre(x: str):
    # Leer el DataFrame desde el archivo CSV
    dataframe = pd.read_csv("ETL/03 - Dataframe para funciones/UserForGenre.csv")

    # Filtrar el DataFrame por el género dado
    genre_df = dataframe.loc[dataframe['Genero'] == x]

    if genre_df.empty:
        return {"error": "No hay datos para el género proporcionado"}

    # Encontrar el usuario con más horas jugadas
    max_hours_user = genre_df.loc[genre_df['Cant_hs_juego'].idxmax()]['Id_user']

    # Agrupar por año y sumar las horas jugadas
    hours_by_year = genre_df.groupby('Año_Lanzamiento')['Cant_hs_juego'].sum().reset_index()

    # Convertir el resultado a un formato de lista de diccionarios
    hours_list = [{'Año': int(row['Año_Lanzamiento']), 'Horas': int(row['Cant_hs_juego'])} for index, row in hours_by_year.iterrows()]

    # Crear el resultado final en el formato deseado
    result = {"Usuario con más horas jugadas para Género {}".format(x): max_hours_user, "Horas jugadas": hours_list}

    return result


@app.get("/year/{x}",tags=["TOP 3 de juegos más recomendados según el año"])
def UsersRecommend(x):
    # Leer el DataFrame desde el archivo CSV
    dataframe = pd.read_csv("ETL/03 - Dataframe para funciones/UsersRecommend.csv")
    
    # Filtrar el DataFrame por el año dado
    year_df = dataframe[dataframe['Año'] == x ]

    if year_df.empty:
        return {"error": "No hay datos para el año proporcionado"}

    # Ordenar el DataFrame por la cantidad de recomendaciones en orden descendente
    sorted_df = year_df.sort_values(by='Cant_rec', ascending=False)

    # Tomar los tres juegos más recomendados
    top3_games = sorted_df.head(3)['Nombre_juego'].tolist()

    # Convertir el resultado a un formato de lista de diccionarios con los puestos correctos
    result = [{"Puesto {}".format(i + 1): juego} for i, juego in enumerate(top3_games)]

    return result









