from datos_stark_00 import lista_personajes
#import  biblioteca_stark_00 
#from biblioteca_stark_00 import * #importa TODAS LAS FUNCIONES
from biblioteca_stark_00 import (
    mostrar_menu, imprime_nombres_de_heroes, imprime_nombres_y_altura_de_heroes, determina_heroe_mas_alto, obtener_nombre, 
    determina_heroe_mas_bajo, realiza_promedio_de_alturas, muestra_identidad_del_heroe_alto_y_bajo, determina_heroe_mas_pesado,
    determina_heroe_menos_pesado
)
"""
León Sokolowski
León Sokolowski
División H
Grupo Alpha
"""

#J. Construir un menú que permita elegir que dato obtener.

def main_app(lista_heroes: list[dict]):
    """
    Ejecuta todo nuestro programa.
    Recibe: lista de heroes.
    Devuelve: nada.
    """

    while True:
        
        opcion_elegida = mostrar_menu()
        
        match (opcion_elegida):
            case "1": 
                #Si escribimos : import  biblioteca_stark_00
                #biblioteca_stark_00.imprime_nombres_de_heroes(lista_heroes)
                imprime_nombres_de_heroes(lista_heroes)
            case "2":
                imprime_nombres_y_altura_de_heroes(lista_heroes)   
            case "3":
                heroe_mas_alto = determina_heroe_mas_alto (lista_heroes)   
                print(obtener_nombre(heroe_mas_alto))   
            case "4":
                heroe_mas_bajo = determina_heroe_mas_bajo (lista_heroes)
                print(obtener_nombre(heroe_mas_bajo))   
            case "5":
                promedio_alturas = realiza_promedio_de_alturas(lista_heroes)
                print(f"El promedio de alturas es: {promedio_alturas}")   
            case "6":
                muestra_identidad_del_heroe_alto_y_bajo ()   
            case "7":
                heroe_mas_pesado = determina_heroe_mas_pesado (lista_heroes)
                print(f"El heroe mas pesado es: {obtener_nombre(heroe_mas_pesado)}")
                heroe_menos_pesado = determina_heroe_menos_pesado (lista_heroes)
                print(f"El heroe menos pesado es: {obtener_nombre(heroe_menos_pesado)}")  
            case "8":
                break     
            case _:
                print("Opcion incorrecta")  

main_app(lista_personajes) 
        