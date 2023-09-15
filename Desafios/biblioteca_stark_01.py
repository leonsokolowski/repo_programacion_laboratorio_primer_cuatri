from datos_stark import lista_personajes
import os

def crea_filtro_para_genero (lista_heroes : list[dict], genero : str) -> list:
    """
    Crea un filtro en base a la clave "genero" y luego crea una lista con todos los heroes que cumplan con ese filtro.
    Recibe: una lista de diccionarios y un string.
    Devuelve: una lista.
    """
    filtro = lambda heroe: heroe["genero"] == genero
    heroes_filtrados = list(filter(filtro, lista_heroes))
    return  heroes_filtrados

def filtrar_nombre_por_genero (lista_heroes : list[dict], genero : str):
    """
    Recorre la lista y luego imprime los nombres que coincidan con el filtro.
    Recibe: una lista de diccionarios y un string.
    Devuelve: nada.
    """
    for heroe in crea_filtro_para_genero(lista_heroes, genero): 
        print(heroe.get("nombre"))

def determinar_heroe_mas_alto_por_genero (lista_heroes : list[dict], genero : str) -> dict:
    """
    Recorre la lista, determina cual es el heroe mas alto en base al filtro y luego lo guarda.
    Recibe: una lista de diccionarios y un string.
    Devuelve: un diccionario.
    """

    heroe_mas_alto = None
    for heroe in crea_filtro_para_genero(lista_heroes, genero):
        if heroe_mas_alto == None or float(heroe_mas_alto.get("altura")) < float(heroe.get("altura")):
            heroe_mas_alto = heroe
            
    return heroe_mas_alto

def determinar_heroe_mas_bajo_por_genero (lista_heroes : list[dict], genero : str) -> dict:
    """
    Recorre la lista, determina cual es el heroe mas bajo en base al filtro y luego lo guarda.
    Recibe: una lista de diccionarios y un string.
    Devuelve: un diccionario.
    """
    
    heroe_mas_bajo = None
    for heroe in crea_filtro_para_genero(lista_heroes, genero):
        if heroe_mas_bajo == None or float(heroe_mas_bajo.get("altura")) > float(heroe.get("altura")):
            heroe_mas_bajo = heroe
            
    return heroe_mas_bajo

def determinar_altura_promedio_por_genero (lista_heroes : list[dict], genero : str) -> float:
    """
    Realiza un promedio de la altura de los heroes filtrados por genero.
    Recibe: una lista de diccionarios y un string.
    Devuelve: un float.
    """
    acumulador_alturas_por_genero = 0
    cantidad_alturas_por_genero = len(crea_filtro_para_genero(lista_heroes, genero))
    
    for heroe in crea_filtro_para_genero(lista_heroes, genero):
        acumulador_alturas_por_genero += float(heroe.get("altura"))
    
    promedio_alturas_por_genero = acumulador_alturas_por_genero / cantidad_alturas_por_genero
    
    return promedio_alturas_por_genero             

def informar_nombre_heroes_mas_altos_y_mas_bajos (lista_heroes):
    """
    Obtiene el nombre de los héroes y heroínas más altos y más bajos y los muestra.
    Recibe: una lista.
    Devuelve: nada
    """ 
    nombre_m_mas_alto = determinar_heroe_mas_alto_por_genero(lista_heroes, "M").get("nombre")
    nombre_f_mas_alta = determinar_heroe_mas_alto_por_genero(lista_heroes, "F").get("nombre")
    nombre_m_mas_bajo = determinar_heroe_mas_bajo_por_genero(lista_heroes, "M").get("nombre")
    nombre_f_mas_baja = determinar_heroe_mas_bajo_por_genero(lista_heroes, "F").get("nombre")
    
    mensaje = f"El nombre del héroe más alto es: {nombre_m_mas_alto}.\n\
    El nombre de la heroína más alta es: {nombre_f_mas_alta}.\n\
    El nombre del héroe más bajo es: {nombre_m_mas_bajo}.\n\
    El nombre de la heroína más baja es: {nombre_f_mas_baja}."
    print(mensaje)

def cantidad_heroes_por_color_ojos (lista_heroes : list[dict]) -> dict:
    """
    Itera la lista de heroes y guarda los colores de ojos y las veces que se repiten.
    Recibe: una lista de diccionarios.
    Devuelve: un diccionario.
    """
        
    color_cantidad_ojos = {}
        
    for heroe in lista_heroes:
        color = heroe.get("color_ojos", "Sin color")
        if not color in color_cantidad_ojos.keys():
            color_cantidad_ojos[color] = 1
        else:
            color_cantidad_ojos[color] += 1
    
    return color_cantidad_ojos

def cantidad_heroes_por_color_pelo (lista_heroes : list[dict]) -> dict:
    """
    Itera la lista de heroes y guarda los colores de pelo y las veces que se repiten.
    Recibe: una lista de diccionarios.
    Devuelve: un diccionario.
    """
    color_cantidad_pelo = {}
        
    for heroe in lista_heroes:
        color = heroe.get("color_pelo", "Sin color")
        if not color in color_cantidad_pelo.keys():
            color_cantidad_pelo[color] = 1
        else:
            color_cantidad_pelo[color] += 1
    
    return color_cantidad_pelo
  
def cantidad_heroes_por_tipo_de_inteligencia (lista_heroes : list[dict]) -> dict:
    """
    Itera la lista de heroes y guarda los tipos de inteligencia y las veces que se repiten.
    Recibe: una lista de diccionarios.
    Devuelve: un diccionario.
    """
    tipo_cantidad_inteligencia = {}
        
    for heroe in lista_heroes:
        tipo = heroe.get("inteligencia", "Sin color")
        if tipo == "":
            tipo = "No tiene"
        
        if not tipo in tipo_cantidad_inteligencia.keys():
            tipo_cantidad_inteligencia[tipo] = 1
        else:
            tipo_cantidad_inteligencia[tipo] += 1

    return tipo_cantidad_inteligencia

def obtener_diccionario_por_color_ojos (lista_heroes : list[dict]) -> dict:
    """
    Obtiene diccionario donde las claves son los colores de ojos y los valores son listas vacías.
    Recibe: una lista de diccionarios.
    Devuelve: un diccionario
    """
    diccionario_color_ojos = {}
        
    for heroe in lista_heroes:
        color = heroe.get("color_ojos", "Sin color")
        diccionario_color_ojos[color] = []

    
    return diccionario_color_ojos

def enlistar_heroes_por_color_ojos (diccionario : dict, lista_heroes : list[dict]) -> dict:
    """
    En base al diccionario previamente creado, le asigna valores a las listas vacías.
    Recibe: un diccionario y un lista de diccionarios.
    Devuelve: un diccionario.
    """
    diccionario = obtener_diccionario_por_color_ojos(lista_heroes)
    
    for heroe in lista_heroes:
        color = heroe.get("color_ojos")
        nombre = heroe.get("nombre")
        diccionario[color].append(nombre)
    
    return diccionario  

def mostrar_lista_heroes_por_color_ojos (diccionario: dict):
    """
    Recorre el diccionario imprimiendo un mensaje en base a la clave y el valor que este iterando.
    Recibe: un diccionario.
    Devuelve: nada.
    """
    for clave, valor in diccionario.items():
        mensaje = f"Los heroes con los ojos color {clave} son {valor}"
        print(mensaje)

def obtener_diccionario_por_color_pelo (lista_heroes : list[dict]) -> dict:
    """
    Obtiene diccionario donde las claves son los colores de pelo y los valores son listas vacías.
    Recibe: una lista de diccionarios.
    Devuelve: un diccionario
    """
    diccionario_color_pelo = {}
        
    for heroe in lista_heroes:
        color = heroe.get("color_pelo", "Sin color")
        diccionario_color_pelo[color] = []

    
    return diccionario_color_pelo

def enlistar_heroes_por_color_pelo (diccionario : dict, lista_heroes : list[dict]) -> dict:
    """
    En base al diccionario previamente creado, le asigna valores a las listas vacías.
    Recibe: un diccionario y un lista de diccionarios.
    Devuelve: un diccionario.
    """
    diccionario = obtener_diccionario_por_color_pelo(lista_heroes)
    
    for heroe in lista_heroes:
        color = heroe.get("color_pelo")
        nombre = heroe.get("nombre")
        diccionario[color].append(nombre)
    
    return diccionario  

def mostrar_lista_heroes_por_color_pelo (diccionario: dict):
    """
    Recorre el diccionario imprimiendo un mensaje en base a la clave y el valor que este iterando.
    Recibe: un diccionario.
    Devuelve: nada.
    """
    for clave, valor in diccionario.items():
        mensaje = f"Los heroes con el pelo color {clave} son {valor}"
        print(mensaje)

def obtener_diccionario_por_tipo_inteligencia (lista_heroes : list[dict]) -> dict:
    """
    Obtiene diccionario donde las claves son los niveles de inteligencia y los valores son listas vacías.
    Recibe: una lista de diccionarios.
    Devuelve: un diccionario
    """
    diccionario_tipo_inteligencia = {}
        
    for heroe in lista_heroes:
        tipo = heroe.get("inteligencia", "Sin tipo")
        diccionario_tipo_inteligencia[tipo] = []

    
    return diccionario_tipo_inteligencia

def enlistar_heroes_por_tipo_inteligencia (diccionario : dict, lista_heroes : list[dict]) -> dict:
    """
    En base al diccionario previamente creado, le asigna valores a las listas vacías.
    Recibe: un diccionario y un lista de diccionarios.
    Devuelve: un diccionario.
    """
    diccionario = obtener_diccionario_por_tipo_inteligencia(lista_heroes)
    
    for heroe in lista_heroes:
        tipo = heroe.get("inteligencia")
        nombre = heroe.get("nombre")
        diccionario[tipo].append(nombre)
    
    return diccionario  

def mostrar_lista_heroes_por_tipo_inteligencia (diccionario: dict):
    """
    Recorre el diccionario imprimiendo un mensaje en base a la clave y el valor que este iterando.
    Recibe: un diccionario.
    Devuelve: nada.
    """
    for clave, valor in diccionario.items():
        mensaje = f"Los heroes con el nivel de intelgencia {clave} son {valor}"
        print(mensaje)

def pedir_opcion_menu () -> str: 
    return input("Elija una opcion: ")

def mostrar_menu_1():
    """
    Muestra el menu con la mitad de nuestras consignas.
    Recibe: lista de heroes.
    Devuelve: nada.
    """
    menu = \
    """
    1. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M.
    2. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
    3. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
    4. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
    5. Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M 
    6. Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F
    7. Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
    8. Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
    9. Salir
    """
    
    print(menu)
    return pedir_opcion_menu()

def mostrar_menu_2():
    """
    Muestra el menu con la mitad de nuestras consignas.
    Recibe: lista de heroes.
    Devuelve: nada.
    """
    menu = \
    """
    1. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores.
    2. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
    3. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
    4. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).
    5. Listar todos los superhéroes agrupados por color de ojos.
    6. Listar todos los superhéroes agrupados por color de pelo.
    7. Listar todos los superhéroes agrupados por tipo de inteligencia
    8. Salir
    """
    
    print(menu)
    return pedir_opcion_menu()

def limpiar_consola() -> None:
    """
    Imprime un mensaje indicando que limpiará la consola al presionar la tecla enter.
        Para que funcione hay que importar el modulo os de la siguiente manera:
        import os
    Recibe: Nada
    Devuelve: Nada
    """
    _ = input("\nPresione enter para continuar... ")
    if os.name in ['ce', 'nt', 'dos']:
        os.system('cls')
    else:
        os.system('clear')

# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M

# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F

# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
 
# D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
 
# E. Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M 

# F. Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F

# G. Recorrer la lista y determinar la altura promedio de los  superhéroes de género M

# H. Recorrer la lista y determinar la altura promedio de los  superhéroes de género F

# I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)

# J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.

# K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.

# L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’). 

# M. Listar todos los superhéroes agrupados por color de ojos.

# N. Listar todos los superhéroes agrupados por color de pelo.

# O. Listar todos los superhéroes agrupados por tipo de inteligencia
