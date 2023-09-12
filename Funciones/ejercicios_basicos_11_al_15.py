"""
11. Crea una función que reciba como parámetro una cadena de texto y devuelva la cantidad de vocales que tiene.
"""

"""
12. Crea una función que reciba dos listas de nombres, y devuelva una lista con los nombres que aparecen en ambas listas
"""

"""
13. Crear una función que recibe una lista de palabras y devuelve un diccionario con las palabras como llaves y su longitud como valores.
"""

lista_de_palabras = ["agua" , "elefante" , "traumatología" , "onomatopeya"]

def retorna_diccionario_y_cantidad_de_letras ( lista_palabras : list) -> dict:
    
    diccionario_de_palabras = {}
    for palabra in lista_palabras:
        diccionario_de_palabras[palabra] = len(palabra)
        
    return diccionario_de_palabras

diccionario_de_palabras_1 = retorna_diccionario_y_cantidad_de_letras(lista_de_palabras)

for clave, valor in diccionario_de_palabras_1.items():
    mensaje = f"La palabra {clave} tiene {valor} letras"
    print(mensaje)

"""
14. Crear una función que recibe una lista de números y devuelve un diccionario con el valor mínimo, 
el valor máximo y el promedio de los números en la lista.
"""

"""
15.Crear una función que recibe una lista de diccionarios con información de películas (título, género, director) 
y devuelve un diccionario con la cantidad de películas por género.
"""

lista_de_info_de_peliculas = [
    {
        "titulo" : "Spiderman 2",
        "genero" : "Acción",
        "director" : "Sam Raimy"
    },
    {
        "titulo" : "Terminator 2",
        "genero" : "Acción",
        "director" : "James Cameron"
    },
    {
        "titulo" : "Spiderman Across the Spiderverse",
        "genero" : "Animación",
        "director" : "Joaquim Dos Santos"
    },
    {
        "titulo" : "Holw's moving castle",
        "genero" : "Animación",
        "director" : "Hayao Miyazaki"
    },
    {
        "titulo" : "Forest Gump",
        "genero" : "Drama",
        "director" : "Robert Zemeckis"
    }
]

def devuelve_cantidad_de_peliculas_por_genero (lista_peliculas: list[dict]) -> dict:
    
    informe_cantidades = {}
    
    for pelicula in lista_peliculas:
        genero = pelicula.get("genero", "Sin genero")
        if not genero in informe_cantidades.keys():
            informe_cantidades[genero] = 1
        else:
            informe_cantidades[genero] += 1
    
    return informe_cantidades 


# def devuelve_cantidad_de_peliculas_por_genero_2 (lista_peliculas: list[dict]) -> dict:
    
#     informe_cantidades = {}
    
#     for pelicula in lista_peliculas:
#         genero = pelicula.get("genero", "Sin genero")
#         informe_cantidades[genero] = informe_cantidades.get(genero, 0) + 1
    
#     return informe_cantidades 

informe = devuelve_cantidad_de_peliculas_por_genero (lista_de_info_de_peliculas)
print(informe)
# informe_2 = devuelve_cantidad_de_peliculas_por_genero_2 (lista_de_info_de_peliculas)
# print(informe_2)