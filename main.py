from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import pandas as pd
import numpy as np
import zipfile

app = FastAPI(title='Proyecto Individual',
            description='Autor:  Atencio Marcelo')


@app.get("/genero/{x}",tags=["Año de lanzamiento con más horas jugadas según el género"])
def PlayTimeGenre(x: str):
    
    """
    
        Esta Funcion devuelve el año con más horas jugadas para dicho género \n
        éstos son algunos de los géneros a investigar \n
	    'Adventure', 'Action', 'Indie', entre otros \n

     
    """

    zip_file = 'PI_1.zip'
    
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall('../data/')  # Descomprime los archivos en el directorio '../data/'

    # Cargar el archivo CSV en un DataFrame
    df = pd.read_csv("../data/PlayTimeGenre.csv")

    # Filtrar el DataFrame para el género específico
    df_genero = df.loc[df['Genero'] == x]

    # Encontrar el año con más horas jugadas para ese género
    año_max_playtime = df_genero.loc[df_genero['playtime_forever'].idxmax(), 'Año_Lanzamiento']

    # Crear la leyenda
    leyenda = f"Año de lanzamiento con más horas jugadas para Género {x}: {año_max_playtime}"

    return leyenda

@app.get("/genero_user/{x}",tags=["Usuario con más horas jugadas según el género"])
def UserForGenre(x: str):

    """
    
        Esta Funcion devuelve el el usuario con más horas jugadas para dicho género y \n
        una lista de la acumulación de horas jugadas por año \n
        éstos son algunos de los géneros a investigar \n
	    'Adventure', 'Action', 'Indie', entre otros \n

     
    """

    zip_file = 'PI_1.zip'
    
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall('../data/')  # Descomprime los archivos en el directorio '../data/'
    
    
    # Leer el DataFrame desde el archivo CSV
    dataframe = pd.read_csv("../data/UserForGenre.csv")

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


@app.get("/year_top3/{x}",tags=["TOP 3 de juegos más recomendados según el año"])
def UsersRecommend(x: int):

    """
    
        Esta Funcion devuelve el TOP 3 de juegos más recomendados por los usuarios para dicho año \n
        éstos son algunos de los años a investigar \n
	    '2015', '2011', '2017', entre otros \n

     
    """

    zip_file = 'PI_1.zip'
    
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall('../data/')  # Descomprime los archivos en el directorio '../data/'
          
    # Leer el DataFrame desde el archivo CSV
    dataframe = pd.read_csv("../data/UsersRecommend.csv")
    
    # Filtrar el DataFrame por el año dado
    year_df = dataframe.loc[dataframe['Año'] == x ]

    if year_df.empty:
        return {"error": "No hay datos para el año proporcionado"}

    # Ordenar el DataFrame por la cantidad de recomendaciones en orden descendente
    sorted_df = year_df.sort_values(by='Cant_rec', ascending=False)

    # Tomar los tres juegos más recomendados
    top3_games = sorted_df.head(3)['Nombre_juego'].tolist()

    # Convertir el resultado a un formato de lista de diccionarios con los puestos correctos
    result = [{"Puesto {}".format(i + 1): juego} for i, juego in enumerate(top3_games)]

    return result

@app.get("/year_bottom3/{x}",tags=["TOP 3 de juegos menos recomendados según el año"])
def UsersNotRecommend(x: int):

    """
    
        Esta Funcion devuelve el TOP 3 de juegos menos recomendados por los usuarios para dicho año \n
        éstos son algunos de los años a investigar \n
	    '2015', '2011', '2017', entre otros \n

     
    """

    zip_file = 'PI_1.zip'
    
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall('../data/')  # Descomprime los archivos en el directorio '../data/'        
        
    # Leer el DataFrame desde el archivo CSV
    dataframe = pd.read_csv("../data/UsersNotRecommend.csv")

    # Filtrar el DataFrame por el año dado
    year_df = dataframe.loc[dataframe['Año'] == x]

    if year_df.empty:
        return {"error": "No hay datos para el año proporcionado"}

    # Ordenar el DataFrame por la cantidad de recomendaciones en orden ascendente
    sorted_df = year_df.sort_values(by='Cant_rec')

    # Tomar los tres juegos menos recomendados
    bottom3_games = sorted_df.head(3)['Nombre_juego'].tolist()

    # Convertir el resultado a un formato de lista de diccionarios con los puestos correctos
    result = [{"Puesto {}".format(i + 1): juego} for i, juego in enumerate(bottom3_games)]

    return result

@app.get("/year_coment/{x}",tags=["Cantidad de comentarios positivos, neutros y negativos según el año"])
def sentiment_analysis(x: int):

    """
    
        Esta Funcion devuelve segun el año de lanzamiento, una lista con la cantidad \n
        de registros de reseñas de usuarios que se encuentran categorizados segun sentimientos \n
        éstos son algunos de los años a investigar \n
	    '2017', '2011', '2015', entre otros \n

     
    """

    zip_file = 'PI_1.zip'
    
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall('../data/')  # Descomprime los archivos en el directorio '../data/'           
        
    # Leer el DataFrame desde el archivo CSV
    dataframe = pd.read_csv("../data/sentiment_analysis.csv")

    # Filtrar el DataFrame por el año dado
    df_filtrado = dataframe[dataframe['Año_Lanzamiento'] == x]
    
    # Agrupar por análisis de sentimiento y sumar la cantidad de registros
    resultados = df_filtrado.groupby('sentiment_analysis')['Cant_reg'].sum().to_dict()

    # Mapear el valor numérico de sentimiento a su correspondiente etiqueta
    resultados = {
        'Negative': resultados.get(0, 0),
        'Neutral': resultados.get(1, 0),
        'Positive': resultados.get(2, 0)
    }

    return resultados

@app.get("/juego_recomm/{x}",tags=["Top 5 juegos recomendados según el ID en cuestión"])
async def recomendacion_juego(x: str):

    """
    
        Esta Funcion devuelve según el ID del usuario, una lista con los 5 juegos recomendados \n
        para dicho usuario \n
        éstos son algunos de los id a investigar \n
	    '350330', '466000', '355970', entre otros \n

     
    """

    zip_file = 'PI_1.zip'
    
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall('../data/')  # Descomprime los archivos en el directorio '../data/'           
        
    # Leer el DataFrame desde el archivo CSV
    dataframe = pd.read_csv("../data/recomendacion_juego.csv")
    dataframe = dataframe.set_index('Nombre_juego')

    ##Obtener la columna correspondiente al juego dado
    columna_juego = dataframe[x]
    
    # Obtener los juegos con los mejores puntajes (menores que 1)
    Juegos = columna_juego[columna_juego < 1.0].sort_values(ascending=False).head(5).index.tolist()

    return f"Juegos recomendados similares a ID n°'{x}': {Juegos}"



