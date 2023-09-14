from datos_stark import lista_personajes

#A

#B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe

def obtener_nombre (heroe: dict) -> str:
    """
    Obtiene el nombre del heroe del diccionario.
    Recibe: diccionario de heroe.
    Devuelve: El valor de la clave "nombre" en string
    """
    nombre = heroe.get("nombre")
    return nombre

def imprime_nombres_de_heroes (lista_heroes : list[dict]):
    """
    Imprime el nombre de todos los heroes de la lista de diccionarios.
    Recibe: cada indice de la lista de diccionarios.
    Devuelve: nada.
    """
    for heroe in lista_heroes:
        nombre = obtener_nombre(heroe)
        print(nombre)



#C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo

def imprime_nombres_y_altura_de_heroes (lista_heroes : list[dict]):
    """
    Imprime el nombre y la altura de todos los heroes de la lista de diccionarios.
    Recibe: cada indice de la lista de diccionarios.
    Devuelve: nada.
    """
    for heroe in lista_heroes:
        nombre = obtener_nombre(heroe)
        altura = heroe.get("altura")
        mensaje = f"Nombre: {nombre} | Altura: {altura}"
        print(mensaje)



#D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)

def determina_heroe_mas_alto (lista_heroes : list[dict]) -> dict :
    """
    Determina cual de todos los heroes es el mas alto.
    Recibe: cada indice de la lista de diccionarios. 
    Devuelve: el mayor valor de altura de los diccionarios de la lista.
    """
    heroe_mas_alto = None
    
    for heroe in lista_heroes:
        if heroe_mas_alto == None or float(heroe_mas_alto.get("altura")) < float(heroe.get("altura")):
            heroe_mas_alto = heroe
    
    return heroe_mas_alto




#E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)

def determina_heroe_mas_bajo (lista_heroes : list[dict]) -> dict :
    """
    Determina cual de todos los heroes es el mas bajo.
    Recibe: cada indice de la lista de diccionarios. 
    Devuelve: el menor valor de altura de los diccionarios de la lista.
    """
    heroe_mas_bajo = None
    
    for heroe in lista_heroes:
        if heroe_mas_bajo == None or float(heroe_mas_bajo.get("altura")) > float(heroe.get("altura")):
            heroe_mas_bajo = heroe
    
    return heroe_mas_bajo



#F. Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)

def realiza_promedio_de_alturas (lista_heroes : list[dict]) -> float:
    """
    Realiza un promedio de todas las alturas de los heroes.
    Recibe: cada indice de la lista de diccionarios. 
    Devuelve: la suma de todas las alturas, dividida entre la cantidad de heroes total.
    """
    cantidad_de_alturas = len(lista_heroes)
    acumulador_alturas = 0
    for heroe in lista_heroes:
        acumulador_alturas += float(heroe.get("altura"))
        
    promedio_alturas = acumulador_alturas / cantidad_de_alturas
    
    return promedio_alturas



#G. Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)

def obtener_identidad (heroe: dict) -> str:
    """
    Obtiene la identidad del heroe del diccionario.
    Recibe: diccionario de heroe.
    Devuelve: El valor de la clave "identidad" en string
    """
    identidad = heroe.get("identidad")
    return identidad

def muestra_identidad_del_heroe_alto_y_bajo (lista_heroes : list):
  """
  Muestra la identidad del heroe más alto y del heroe más bajo.
  Recibe: nada.
  Devuelve: nada.
  """
  mensaje = f"La identidad del heroe más alto es: {obtener_identidad(determina_heroe_mas_alto(lista_heroes))}\n\
  La identidad del heroe más bajo es: {obtener_identidad(determina_heroe_mas_bajo(lista_heroes))}"
  print(mensaje)

#H. Calcular e informar cual es el superhéroe más y menos pesado.

def determina_heroe_mas_pesado (lista_heroes : list[dict]) -> dict :
    """
    Determina cual de todos los heroes es el mas pesado.
    Recibe: cada indice de la lista de diccionarios. 
    Devuelve: el mayor valor de peso de los diccionarios de la lista.
    """
    heroe_mas_pesado = None
    
    for heroe in lista_heroes:
        if heroe_mas_pesado == None or float(heroe_mas_pesado.get("peso")) < float(heroe.get("peso")):
            heroe_mas_pesado = heroe
    
    return heroe_mas_pesado



def determina_heroe_menos_pesado (lista_heroes : list[dict]) -> dict :
    """
    Determina cual de todos los heroes es el menos pesado.
    Recibe: cada indice de la lista de diccionarios. 
    Devuelve: el menor valor de peso de los diccionarios de la lista.
    """
    heroe_menos_pesado = None
    
    for heroe in lista_heroes:
        if heroe_menos_pesado == None or float(heroe_menos_pesado.get("peso")) > float(heroe.get("peso")):
            heroe_menos_pesado = heroe
    
    return heroe_menos_pesado



#I.
#J. Construir un menú que permita elegir que dato obtener.

def pedir_opcion_menu () -> str:
    return input("Elija una opcion: ")
def mostrar_menu() -> str:
    """
    Ejecuta todo nuestro programa.
    Recibe: lista de heroes.
    Devuelve: nada.
    """
    menu = \
    """
    1. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
    2. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
    3. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
    4. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
    5. Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
    6. Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
    7. Calcular e informar cual es el superhéroe más y menos pesado.
    8. Salir
    """
    
    print(menu)
    return pedir_opcion_menu()
    