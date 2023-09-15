from datos_stark import lista_personajes
from biblioteca_stark_01 import (
    filtrar_nombre_por_genero, determinar_heroe_mas_alto_por_genero, determinar_heroe_mas_bajo_por_genero,
    determinar_altura_promedio_por_genero, informar_nombre_heroes_mas_altos_y_mas_bajos, cantidad_heroes_por_color_ojos,
    cantidad_heroes_por_color_pelo, cantidad_heroes_por_tipo_de_inteligencia, obtener_diccionario_por_color_ojos,
    enlistar_heroes_por_color_ojos, mostrar_lista_heroes_por_color_ojos, obtener_diccionario_por_color_pelo,
    enlistar_heroes_por_color_pelo, mostrar_lista_heroes_por_color_pelo, obtener_diccionario_por_tipo_inteligencia,
    enlistar_heroes_por_tipo_inteligencia, mostrar_lista_heroes_por_tipo_inteligencia, mostrar_menu_1, mostrar_menu_2, limpiar_consola
    )


def main_app_1(lista_heroes: list[dict]):
    """
    Ejecuta la mitad de nuestro programa.
    Recibe: lista de heroes.
    Devuelve: nada.
    """

    while True:
        
        opcion_elegida = mostrar_menu_1()
        
        match (opcion_elegida):
            case "1": 
                filtrar_nombre_por_genero (lista_heroes , "M")
            case "2":
                filtrar_nombre_por_genero (lista_heroes , "F")   
            case "3":
                print(determinar_heroe_mas_alto_por_genero(lista_heroes, "M"))    
            case "4":
                print(determinar_heroe_mas_alto_por_genero(lista_heroes, "F"))   
            case "5":
                print(determinar_heroe_mas_bajo_por_genero(lista_heroes, "M"))   
            case "6":
                print(determinar_heroe_mas_bajo_por_genero(lista_heroes, "F"))   
            case "7":
                print(determinar_altura_promedio_por_genero(lista_heroes, "M"))  
            case "8":
                print(determinar_altura_promedio_por_genero(lista_heroes, "F"))
            case "9":
                break     
            case _:
                print("Opcion incorrecta")  
        limpiar_consola()

def main_app_2(lista_heroes: list[dict]):
    """
    Ejecuta la mitad de nuestro programa.
    Recibe: lista de heroes.
    Devuelve: nada.
    """

    while True:
        
        opcion_elegida = mostrar_menu_2()
        
        match (opcion_elegida):
            case "1": 
                informar_nombre_heroes_mas_altos_y_mas_bajos(lista_heroes)
            case "2":
                print(cantidad_heroes_por_color_ojos(lista_heroes))   
            case "3":
                print(cantidad_heroes_por_color_pelo(lista_heroes))
            case "4":
                print(cantidad_heroes_por_tipo_de_inteligencia(lista_heroes))   
            case "5":
                mostrar_lista_heroes_por_color_ojos(enlistar_heroes_por_color_ojos(obtener_diccionario_por_color_ojos(lista_heroes),lista_heroes))   
            case "6":
                mostrar_lista_heroes_por_color_pelo(enlistar_heroes_por_color_pelo(obtener_diccionario_por_color_pelo(lista_heroes),lista_heroes))   
            case "7":
                mostrar_lista_heroes_por_tipo_inteligencia(enlistar_heroes_por_tipo_inteligencia(obtener_diccionario_por_tipo_inteligencia(lista_heroes),lista_heroes))  
            case "8":
                break   
            case _:
                print("Opcion incorrecta")  
        limpiar_consola()
