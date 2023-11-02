import os
import re
from clase_equipo import Equipo, ruta_de_csv

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
        
def imprimir_menu ():
    """
    Imprime un menu.
    Recibe: nada.
    Devuelve: nada.
    """
    menu = \
    """
    1. Mostrar los nombres y las posiciones de todos los jugadores del Dream Team.
    2. Mostrar las estadísticas de todos los jugadores buscandolos por su indice (Tiene la opción de cargarlas a un CSV).
    3. Buscar jugador por su nombre y mostrar sus logros.
    4. Mostrar el promedio de los promedios de puntos por partido de cada jugador, seguido por un lista ordenada de manera
       ascendente de los jugadores y sus promedios.
    5. Buscar jugador por su nombre y mostrar si pertenece o no al Salon de la Fama del Baloncesto.
    6. Mostrar al jugador con mayor cantidad de rebotes.
    7. Mostrar los nombres y las temporadas de todos los jugadores del Dream Team ordenados de manera descendente segun la 
       cantidad de temporadas que jugó cada uno. (Tiene la opción de cargarlas a un CSV y/o a un JSON)
    8. Ordenar la lista de jugadores de manera descendente en base a la suma de las estadisticas de robos totales y bloqueos
       totales, ademas crea un porcentaje de esta cantidad. Usted elige la cantidad de jugadores que se mostraran.
    9. Salir.
    """
    print(menu)


def dream_team_app (equipo: Equipo) -> None:
    """
    Ejecuta toda nuestra aplicación.
    Recibe: una lista de diccionarios.
    Devuelve: nada.
    """
    
    while True:
        imprimir_menu()
        
        opcion = input("Ingrese el número que desee: ")
        while re.match("[1-9]$", opcion) == None:
            print("Opción incorrecta.")
            opcion = input("Ingrese un número valido: ")
        opcion = int(opcion)
            
        match(opcion):
            case 1:
                equipo.mostrar_todos_los_jugadores_y_su_posicion()
            case 2:
                equipo.seleccionar_jugador_y_mostrar_sus_estadisticas() 
            case 3:
                equipo.seleccionar_jugador_y_mostrar_sus_logros()
            case 4:
                equipo.promedio_de_puntos_por_partido_del_equipo()
            case 5:
                equipo.seleccionar_jugador_y_mostrar_si_pertence_al_sdlf()
            case 6:
                equipo.calcular_y_mostrar_jugador_con_mas_rebotes()
            case 7:
                equipo.listar_jugadores_ordenados_por_la_cantidad_de_temporadas()
            case 8:
                equipo.mostrar_jugadores_robos_mas_bloqueos()
            case 9:
                break
        
        limpiar_consola()

