"""
León Sokolowski
León Sokolowski
División H
Grupo Alpha
"""
"""
11. Crea una función que reciba como parámetro una cadena de texto y devuelva la cantidad de vocales que tiene.
"""
def contador_vocales_por_palabra (palabra : str) -> int:
    """
    Recorre los indices de una palabra y verifica si la letra que lo ocupa es una vocal o no.
    Recibe: un dato string.
    Devuelve: un dato int.
    """
    contador_vocales = 0

    for letra in palabra:
        
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            contador_vocales += 1
    return contador_vocales

"""
12. Crea una función que reciba dos listas de nombres, y devuelva una lista con los nombres que aparecen en ambas listas
"""
lista_de_nombres_1 = ["Mauricio", "Marcos", "Daniela", "Felipe", "Cecilia"]
lista_de_nombres_2 = ["Matias", "Marcos", "Fernanda", "Hector", "Cecilia"]

lista_de_nombres_repetidos = []

def filtro_de_nombres_repetidos (lista_nombres_a : list, lista_nombres_b : list) -> list:
    """
    Filtra en una nueva lista los nombres que se repitan en otras 2 listas.
    Recibe: 2 listas.
    Devuelve: 1 lista.
    """
    for nombre_a in lista_nombres_a:
        for nombre_b in lista_nombres_b:
            if nombre_a == nombre_b:
                lista_de_nombres_repetidos.append(nombre_a)
    
    return lista_de_nombres_repetidos

print(filtro_de_nombres_repetidos(lista_de_nombres_1 , lista_de_nombres_2))

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
lista_de_numeros = [21, 24, 5, 4, 31]

def calculo_valor_min_max_y_promedio (lista_numeros : list) -> dict:
    
    valor_maximo = None
    valor_minimo = None
    acumulador_valores = 0
    cantidad_numeros = len(lista_numeros)
    diccionario_valores_finales = {}
    
    for numero in lista_numeros:
        
        if valor_maximo == None or numero > valor_maximo:
            valor_maximo = numero
            diccionario_valores_finales["valor maximo"] = valor_maximo
        
        if valor_minimo == None or numero < valor_minimo:
            valor_minimo = numero
            diccionario_valores_finales["valor minimo"] = valor_minimo
        
        acumulador_valores += numero
    
    promedio_valores = acumulador_valores / cantidad_numeros
    diccionario_valores_finales["promedio"] = promedio_valores
    
    return diccionario_valores_finales

print(calculo_valor_min_max_y_promedio(lista_de_numeros))

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