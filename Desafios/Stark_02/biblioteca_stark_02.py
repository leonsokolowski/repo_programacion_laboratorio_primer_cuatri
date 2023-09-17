from datos_stark import lista_personajes

#0
def normalizar_datos_stark (lista_heroes : list[dict]):
    """
    Recorre los diccionarios de la lista, y cambia el tipo de dato de los valores de las claves que representan números.
    Recibe: una lista de diccionarios.
    Devuelve: nada.
    """
    for heroe in lista_heroes:
        if lista_heroes == []:
            mensaje = "Error: Lista de héroes vacía"
        else:    
            altura = heroe.get("altura")
            if altura != float:
                altura = float
                mensaje = "Datos normalizados"
            
            peso = heroe.get("peso")
            if peso != float:
                peso = float
                mensaje = "Datos normalizados"
                
            fuerza = heroe.get("fuerza")
            if fuerza != int:
                fuerza = int
                mensaje = "Datos normalizados"
    print(mensaje)

#1.1
def obtener_nombre (heroe : dict) -> str:
    """
    Obtiene el nombre del heroe que representa el diccionario.
    Recibe: un diccionario.
    Devuelve: un string.
    """
    nombre = heroe.get("nombre")
    return nombre 
#1.2
def imprimir_dato (palabra : str):
    """
    Imprime por consola una palabra.
    Recibe: un string.
    Devuelve: nada.
    """
    print(palabra)    
#1.3
def stark_imprimir_nombres_heroes (lista_heroes : list[dict]):
    """
    Imprime los nombres de todos los heroes de la lista, siempre y cuando la lista no esté vacía.
    Recibe: una lista de diccionarios.
    Devuelve: nada.
    """
    if lista_heroes == []:
        print("ERROR: Lista vacía.")
    else:
        for heroe in lista_heroes:
            imprimir_dato(obtener_nombre(heroe))

#2
def obtener_nombre_y_dato (heroe : dict, clave : str) -> str:
    """
    Obtiene el nombre de un heroe y el valor de la clave que se ingrese. Luego, los coloca en un mensaje.
    Recibe: un dicionario y un string.
    Devuelve: un string 
    """
    nombre = obtener_nombre(heroe)
    dato = heroe.get(clave)
    
    mensaje = f"Nombre: {nombre} | {clave}: {dato}"
    return mensaje

#3
def stark_imprimir_nombres_alturas(lista_heroes : list[dict]):
    """
    Recorre la lista e imprime los nombres y las alturas de los heroes de la lista, siempre y cuando esta no esté vacía.
    Recibe: una lista de diccionarios.
    Devuelve: nada.
    """
    if lista_heroes == []:
        print("ERROR: Lista vacía.")
    else:
        for heroe in lista_heroes:
            print(obtener_nombre_y_dato(heroe, "altura"))

#4.1




        








if __name__ == "__main__":
    #normalizar_datos_stark (lista_personajes)
    #imprimir_dato("cacao")
    # A. Analizar detenidamente el set de datos
    
    # B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
    stark_imprimir_nombres_heroes(lista_personajes)
    
    # C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
    stark_imprimir_nombres_alturas(lista_personajes)
    
    # D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
    # E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
    # F. Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
    # G. Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
    # H. Calcular e informar cual es el superhéroe más y menos pesado.
    # I. Ordenar el código implementando una función para cada uno de los valores informados.
    # J. Construir un menú que permita elegir qué dato obtener
