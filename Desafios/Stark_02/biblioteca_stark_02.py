from datos_stark import lista_personajes
import os
#0
def normalizar_datos_stark (lista_heroes : list[dict]):
    """
    Recorre los diccionarios de la lista, y cambia el tipo de dato de los valores de las claves que representan números.
    Recibe: una lista de diccionarios.
    Devuelve: nada.
    """
    if lista_heroes == []:
        mensaje = "Error: Lista de héroes vacía"
    else:    
        for heroe in lista_heroes:
            altura = heroe.get("altura")
            if type(altura) != float:
                altura = float(altura)
                heroe.update({"altura" : altura})
                mensaje = "Datos normalizados"
            
            peso = heroe.get("peso")
            if type(peso) != float:
                peso = float(peso)
                heroe.update({"peso" : peso}) 
                mensaje = "Datos normalizados"
                
            fuerza = heroe.get("fuerza")
            if type(fuerza) != int:
                fuerza = int(fuerza)
                heroe.update({"fuerza" : fuerza})
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
def obtener_identidad (heroe : dict) -> str:
    """
    Obtiene la identidad del heroe que representa el diccionario.
    Recibe: un diccionario.
    Devuelve: un string.
    """
    identidad = heroe.get("identidad")
    return identidad 
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
        print("-1")
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
def obtener_identidad_y_dato (heroe : dict, clave : str) -> str:
    """
    Obtiene la identidad de un heroe y el valor de la clave que se ingrese. Luego, los coloca en un mensaje.
    Recibe: un dicionario y un string.
    Devuelve: un string 
    """
    identidad = obtener_identidad(heroe)
    dato = heroe.get(clave)
    
    mensaje = f"Identidad: {identidad} | {clave}: {dato}"
    return mensaje
#3
def stark_imprimir_nombres_alturas(lista_heroes : list[dict]):
    """
    Recorre la lista e imprime los nombres y las alturas de los heroes de la lista, siempre y cuando esta no esté vacía.
    Recibe: una lista de diccionarios.
    Devuelve: nada.
    """
    if lista_heroes == []:
        print("-1")
    else:
        for heroe in lista_heroes:
            print(obtener_nombre_y_dato(heroe, "altura"))

#4.1
def calcular_max (lista_heroes : list[dict] , clave : str) -> dict:
    """
    Normaliza los datos, recorre la lista de heroes y determina el máximo de la categoría ingresada como clave.
    Recibe: una lista de diccionarios y un string.
    Devuelve: un diccionario.
    """

    heroe_maximo= None
    
    for heroe in lista_heroes:
        if heroe_maximo == None or heroe_maximo.get(clave) < heroe.get(clave):
            heroe_maximo = heroe
    
    return heroe_maximo
def calcular_min (lista_heroes : list[dict] , clave : str) -> dict:
    """
    Normaliza los datos, recorre la lista de heroes y determina el mínimo de la categoría ingresada como clave.
    Recibe: una lista de diccionarios y un string.
    Devuelve: un diccionario.
    """
    minimo = None
    
    for heroe in lista_heroes:
        if minimo == None or minimo.get(clave) > heroe.get(clave):
            minimo = heroe
    
    return minimo
#4.3
def calcular_max_min_dato (lista_heroes : list[dict] , tipo_de_calculo : str , clave : str) -> dict:
    """
    Calcula el maximo o el minimo de una clave.
    Recibe: una lista de diccionarios y dos strings para poder filtrar.
    Devuelve: un diccionario
    """
    
    match(tipo_de_calculo):
        case "maximo":
            match(clave):
                case "altura":
                    heroe = calcular_max(lista_heroes , "altura")
                case "peso":
                    heroe = calcular_max(lista_heroes , "peso")
                case "fuerza":
                    heroe = calcular_max(lista_heroes , "fuerza")
        case "minimo":
            match(clave):
                case "altura":
                    heroe = calcular_min(lista_heroes , "altura")
                case "peso":
                    heroe = calcular_min(lista_heroes , "peso")
                case "fuerza":
                    heroe = calcular_min(lista_heroes , "fuerza")
    
    return heroe
#4.4
def stark_calcular_imprimir_heroe (lista_heroes : list[dict] , tipo_de_calculo : str , clave : str):
    """
    Obtiene e imprime el nombre del heroe con el maximo o minimo valor de la clave ingresada, siempre y cuando la lista no esté vacía.
    Recibe: una lista de diccionarios y dos strings para poder filtrar.
    Devuelve: nada.
    """
    if lista_heroes == []:
        print("-1")
    else:
        heroe = calcular_max_min_dato(lista_heroes , tipo_de_calculo , clave)
        
        nombre_y_dato = obtener_nombre_y_dato (heroe, clave)
        
        imprimir_dato (nombre_y_dato)
def stark_calcular_imprimir_heroe_identidad (lista_heroes : list[dict] , tipo_de_calculo : str , clave : str):
    """
    Obtiene e imprime la identidad del heroe con el maximo o minimo valor de la clave ingresada, siempre y cuando la lista no esté vacía.
    Recibe: una lista de diccionarios y dos strings para poder filtrar.
    Devuelve: nada.
    """
    if lista_heroes == []:
        print("-1")
    else:
        heroe = calcular_max_min_dato(lista_heroes , tipo_de_calculo , clave)
        
        identidad_y_dato = obtener_identidad_y_dato (heroe, clave)
        
        imprimir_dato (identidad_y_dato)

#5.1
def sumar_dato_heroe (lista_heroes : list[dict], clave : str) -> float:
    """
    Suma los valores de la clave luego de comprobar que el diccionario no está vacío.
    Recibe: una lista de diccionarios y un string.
    Devuelve: un float.
    """
    datos_sumados = 0
    
    for heroe in lista_heroes:
        if type(heroe) != dict or heroe == {}:
            print("ERROR. 'Heroe' no es un diccionario o está vacío")
        else:
            dato = heroe.get(clave)
            datos_sumados += dato
    
    return datos_sumados
#5.2
def dividir (dividendo : float , divisor : int) -> float:
    """
    Divide dos numeros, en caso de que sea una división por 0, devuelve 0.
    Recibe: un float y un int.
    Devuelve: un float.
    """
    if divisor == 0:
        division = 0
    else:
        division = dividendo / divisor

    return division
#5.3
def calcular_promedio (lista_heroes : list[dict], clave : str) -> float:
    """
    Calcula el promedio de los valores de la clave.
    Recibe: una lista de diccionarios y un string.
    Devuelve: un float.
    """
    dividendo = sumar_dato_heroe(lista_heroes , clave)
    divisor = len(lista_heroes)
    
    division = dividir(dividendo , divisor)
    
    return division
#5.4
def stark_calcular_imprimir_promedio_altura (lista_heroes : list[dict]):
    """
    Calcula el promedio de altura de heroes, crea un mensaje con el y lo imprime.
    Recibe: una lista de diccionarios.
    Devuelve: nada.
    """
    promedio = calcular_promedio(lista_heroes , "altura")
    mensaje = f"El promedio de alturas de heroes es de {promedio}"
    imprimir_dato (mensaje)

#6.1
def imprimir_menu ():
    """
    Imprime un menu.
    Recibe: nada.
    Devuelve: nada.
    """
    menu = \
    """
    1. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe.
    2. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo .
    3. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO).
    4. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO).
    5. Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO).
    6. Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO).
    7. Calcular e informar cual es el superhéroe más y menos pesado.
    8. Salir.
    """
    imprimir_dato (menu)
#6.2
def validad_entero (numero_en_string : str) -> bool:
    """
    Comprueba que un dato string que representa un solo digitos numéricos.
    Recibe: un string.
    Devuelve: un bool.
    """
    valor_booleano = None
    
    if numero_en_string.isnumeric() == True:
        valor_booleano = True
    else:
        valor_booleano = False
    
    return valor_booleano
#6.3
def stark_menu_principal () -> int:
    """
    Imprime el menu, pide un número, lo valida, y lo devuelve.
    Recibe: nada.
    Devuelve: un int.
    """
    imprimir_menu() 
    
    numero_elegido = input("Elija una opción: ")
    
    if validad_entero (numero_elegido) == True:
        numero_elegido = int(numero_elegido)
    else:
        numero_elegido = -1
    
    print(numero_elegido)
    return numero_elegido

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
        
#7
def stark_marvel_app (lista_heroes : list[dict]):
    """
    Ejecuta toda nuestra aplicación.
    Recibe: una lista de diccionarios.
    Devuelve: nada.
    """
    normalizar_datos_stark(lista_personajes)
    
    while True:
        
        opciones = stark_menu_principal()
        
        match(opciones):
            case 1:
                stark_imprimir_nombres_heroes(lista_heroes)
            case 2:
                stark_imprimir_nombres_alturas(lista_heroes)
            case 3:
                stark_calcular_imprimir_heroe (lista_heroes, "maximo" , "altura")
            case 4:
                stark_calcular_imprimir_heroe (lista_heroes, "minimo" , "altura")
            case 5:
                stark_calcular_imprimir_promedio_altura(lista_heroes)
            case 6:
                stark_calcular_imprimir_heroe_identidad (lista_heroes, "maximo" , "altura")
                stark_calcular_imprimir_heroe_identidad (lista_heroes, "minimo" , "altura")
            case 7:
                stark_calcular_imprimir_heroe (lista_heroes, "maximo" , "peso")
                stark_calcular_imprimir_heroe (lista_heroes, "minimo" , "peso")
            case 8:
                break
            case _:
                print("Opción incorrecta.")
                opciones
       
        limpiar_consola()
    
    
    
           

if __name__ == "__main__":
    normalizar_datos_stark(lista_personajes)
    # A. Analizar detenidamente el set de datos
    
    # B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
    stark_imprimir_nombres_heroes(lista_personajes)
    
    # C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
    stark_imprimir_nombres_alturas(lista_personajes)
    
    # D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
    stark_calcular_imprimir_heroe (lista_personajes, "maximo" , "altura")
    
    # E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
    stark_calcular_imprimir_heroe (lista_personajes, "minimo" , "altura")
    
    # F. Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
    stark_calcular_imprimir_promedio_altura(lista_personajes)
    
    # G. Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
    stark_calcular_imprimir_heroe_identidad (lista_personajes, "maximo" , "altura")
    stark_calcular_imprimir_heroe_identidad (lista_personajes, "minimo" , "altura")
    
    # H. Calcular e informar cual es el superhéroe más y menos pesado.
    stark_calcular_imprimir_heroe (lista_personajes, "maximo" , "peso")
    stark_calcular_imprimir_heroe (lista_personajes, "minimo" , "peso")
    
    # J. Construir un menú que permita elegir qué dato obtener 
    stark_menu_principal()
    
