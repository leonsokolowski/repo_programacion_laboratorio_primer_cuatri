from datos_stark import lista_personajes

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

def cantidad_heroes_por_color_ojos (lista_heroes : list[dict]):
    
    cantidad_color_ojos = {}

    for heroe in lista_heroes:
        color_ojos = heroe.get("color_ojos")
        cantidad_color_ojos.update({color_ojos : "1"})
        
    

def cantidad_heroes_por_color_pelo ():
    pass

def cantidad_heroes_por_tipo_inteligencia ():
    pass

# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M

filtrar_nombre_por_genero (lista_personajes , "M")

# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F

filtrar_nombre_por_genero (lista_personajes , "F")

# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M

print(determinar_heroe_mas_alto_por_genero(lista_personajes, "M"))        
 
# D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F

print(determinar_heroe_mas_alto_por_genero(lista_personajes, "F"))
 
# E. Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M 

print(determinar_heroe_mas_bajo_por_genero(lista_personajes, "M"))

# F. Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F

print(determinar_heroe_mas_bajo_por_genero(lista_personajes, "F"))

# G. Recorrer la lista y determinar la altura promedio de los  superhéroes de género M

print(determinar_altura_promedio_por_genero(lista_personajes, "M"))

# H. Recorrer la lista y determinar la altura promedio de los  superhéroes de género F

print(determinar_altura_promedio_por_genero(lista_personajes, "F"))

# I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)

informar_nombre_heroes_mas_altos_y_mas_bajos (lista_personajes)

# J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.



# K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.



# L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’). 



# M. Listar todos los superhéroes agrupados por color de ojos.



# N. Listar todos los superhéroes agrupados por color de pelo.



# O. Listar todos los superhéroes agrupados por tipo de inteligencia
