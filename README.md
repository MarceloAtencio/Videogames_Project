
<h4 align=center> PROYECTO INDIVIDUAL Nº1 </h4>

<h2 align=center>Machine Learning Operations (MLOps)</h2>

<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png"  height=150>
</p>


## Enunciado del proyecto

Empezaste a trabajar como **`Data Scientist`** en Steam, una plataforma multinacional de videojuegos. El mundo es bello y vas a crear tu primer modelo de ML que soluciona un problema de negocio: Steam pide que te encargues de crear un sistema de recomendación de videojuegos para usuarios. :worried:

Vas a sus datos y te das cuenta que la madurez de los mismos es poca (ok, es nula :sob: ): Datos anidados, de tipo raw, no hay procesos automatizados para la actualización de nuevos productos, entre otras cosas… haciendo tu trabajo imposible :weary: . 

Debes empezar desde 0, haciendo un trabajo rápido de **`Data Engineer`** y tener un **`MVP`** (_Minimum Viable Product_) para el cierre del proyecto! Tu cabeza va a explotar 🤯, pero al menos sabes cual es, conceptualmente, el camino que debes de seguir :exclamation:. Así que espantas los miedos y pones manos a la obra :muscle:

## Proceso de trabajo

A lo largo del proyecto afronte grandes desafios, como entablecer un pensamiento critico y la capacidad de autogestionarme y ser un autodidacta constante, busque, investigue, racionalice, consulte con por varios canales para encontrar la mejor forma de plasmar todo aprendido.-

Mi repositorio se encuentra establecido de una manera que al descarlo puedan hacer un seguimiento de los procesos y resultados conseguidos sobre los DataSet Originales.-

En resumen, este proyecto consegui la autonomía, la organización, la resolución de problemas, la comunicación escrita, el aprendizaje autodirigido y el pensamiento crítico.

## Exploración y limpieza de datos

Comence creando la carpeta Archivos_DATA, ahi guardo los dataset originales de formato .gz en donde de ahi empieza todo la limpieza.-

A continuacion cree la carpeta ETL en donde tambien hice sub-carpetas en donde hice en forma secuencial todo el ETL:

**01 - Extracción de archivos**: En esta carpeta cree un archivo jupyter que extrae los datos contenidos en los datasets originales, y los almacena en dicha carpeta en formato .csv. En una posterior etapa, ya 	procesados y armados los archivos necesarios para las funciones y el ML, éstos archivos se proceden a borrar debido a su tamaño e imposibilidad de subirlo a GitHub.

**02 - Desanidado de datos y limpieza**: En esta carpeta cree un archivo Jupyter en donde procede a desanidar aquellos datos que son necesarios para posterior analisis y limpieza de datos. Los tres archivos son almacenados en formato csv dentro de la misma carpeta.

**03 - Deataframe para funciones**: En esta carpeta cree dos archivos Jupyter. En el archivo "Dataframe_funciones" realice operaciones de cruce de información entre los tres archivos mencionados anteriormente y asi poder obtener datasetr limpios para cada función (menor cantidad de datos para que el archivo sea menos pesado). Cada archivo de su respectiva funcion es almacenado en formato .csv dentro de la misma carpeta y procedo a comprimir los archivos del punto 02. En el segundo archivo "Dataframe_ML" realice operaciones para el modelado de ML en referencia a plantear un modelo de recomendación de juegos en base a un ID de uno en específico, aplicando similitud de cosenos. Por la gran cantidad de juegos registrados (y por ende el tamaño del archivo) procedi a tomar una muestra del 10% de los datos que permita visualizar el funcionamiento del ML en la API (Render cuenta con poca memoria RAM).

Además cuenta con una carpeta "PI_1" el cual cuenta con los 6 archivos datasets correspondiente a cada función, pero en formato comprimido .zip.

Y los siguientes archivos:

**EDA.ipnyb**: el cual contiene el análisis exploratorio de datos, el cual me permitio definir la variable "Genero" como la indicada para el modelo de ML.

**Funciones.ipnyb**: tiene planteado cada una de las funciones, desarrollo y prueba de las mismas.

**main.py**: archivo py el cual tiene configurado todas las funciones para su lectura por render.

**requirements.txt**: archivo útil para realizar el despliegue en render


## Funciones

El objetivo del proyecto constaba en el planteo, desarrollo y funcionamiento de 6 funciones:

+ def **PlayTimeGenre( *`genero` : str* )**:
    Debe devolver `año` con mas horas jugadas para dicho género.
  
Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}

+ def **UserForGenre( *`genero` : str* )**:
    Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.

Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf,
			     "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}

+ def **UsersRecommend( *`año` : int* )**:
   Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
  
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

+ def **UsersNotRecommend( *`año` : int* )**:
   Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)
  
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

+ def **sentiment_analysis( *`año` : int* )**:
    Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento. 

Ejemplo de retorno: {Negative = 182, Neutral = 120, Positive = 278}


**Modelo de aprendizaje automático**: 

El modelo deberá tener una relación ítem-ítem, esto es se toma un item, en base a que tan similar esa ese ítem al resto, se recomiendan similares. Aquí el input es un juego y el output es una lista de juegos recomendados, para ello recomendamos aplicar la *similitud del coseno*. 

+ def **recomendacion_juego( *`id de producto`* )**:
    Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.


## Links

+ [API](https://proyecto-individual-1-atencio-marcelo.onrender.com/docs): puede demorar varios minutos en cargar completamente.
  
+ [Mi video](https://docs.google.com/spreadsheets/d/1-t9HLzLHIGXvliq56UE_gMaWBVTPfrlTf2D9uAtLGrk/edit?usp=drive_link): video explicativo del proyecto y funcion de API.
  
<br/>
