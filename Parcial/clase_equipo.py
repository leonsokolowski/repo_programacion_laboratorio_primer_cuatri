import json
import re
import csv
import os
from clase_jugador import Jugador

ruta_de_archivo = r"Parcial/dream_team.json"
ruta_de_csv = r"Parcial\basquetbolistas.csv"
 
class Equipo():
    def __init__(self, archivo):
        self.archivo = archivo
        self.lista_de_jugadores = self.crear_jugadores_y_agregarlos_a_lista()
        
        
    def importar_json (self):
        with open(self.archivo, "r", encoding= "utf-8") as jugadores_dream_team:
            diccionario_equipo = json.load(jugadores_dream_team)
        return diccionario_equipo
            
    
    def crear_jugadores_y_agregarlos_a_lista (self):
        lista_de_jugadores = []
        data_jugadores = self.importar_json().get("jugadores")
        for jugador in data_jugadores:
            lista_de_jugadores.append(Jugador(jugador))
        return lista_de_jugadores
    
    #1
    def mostrar_todos_los_jugadores_y_su_posicion (self):
        for jugador in self.lista_de_jugadores:
            nombre = jugador.obtener_nombre_jugador
            posicion = jugador.obtener_posicion_jugador
            print(f"{nombre} - {posicion}")
    
    #2
    def seleccionar_jugador_y_mostrar_sus_estadisticas (self):
        cantidad_de_jugadores = len(self.lista_de_jugadores)
        jugador_seleccionado = input(f"Seleccione un jugador por su índice (1 - {cantidad_de_jugadores}): ")
        
        while re.match("[1-9]+", jugador_seleccionado) == None:
            jugador_seleccionado = input(f"No existe ese jugador_seleccionado. Seleccione un jugador por su índice (1 - {cantidad_de_jugadores}): ")
        if re.match("[1-9]+", jugador_seleccionado):
            jugador_seleccionado = int(jugador_seleccionado) - 1
            if jugador_seleccionado <= cantidad_de_jugadores:
                estadisticas_jugador = self.lista_de_jugadores[jugador_seleccionado].obtener_estadisticas_completas()
                print(self.lista_de_jugadores[jugador_seleccionado].obtener_nombre_jugador)
                for clave, valor in estadisticas_jugador.items():
                    print(f"{clave.capitalize()} : {valor}")
                
                #3
                pregunta_csv = input("¿Querés añadir estas estadisticas a un csv? (Si|No): ").lower()
                while pregunta_csv != "si" and pregunta_csv != "no":
                    pregunta_csv = input("Tiene que responder Si o No: ").lower()
                if pregunta_csv == "si":
                    self.crear_csv(jugador_seleccionado)
                    print("Información enviada exitosamente")
                elif pregunta_csv == "no":
                    print("No se realizará la conversión a csv")
                
    
    #3
    def crear_csv(self, indice):
        nombre = self.lista_de_jugadores[indice].obtener_nombre_jugador
        posicion = self.lista_de_jugadores[indice].obtener_posicion_jugador
        estadisticas = self.lista_de_jugadores[indice].obtener_estadisticas_completas()
        lista_datos = []
        lista_datos.append(nombre)
        lista_datos.append(posicion)
        for v in estadisticas.values():
            lista_datos.append(v)
        if os.path.isfile(ruta_de_csv):
            with open(ruta_de_csv, 'r+', newline='') as archivo:
                lector_csv = csv.reader(archivo)
                lineas = list(lector_csv)
                nueva_linea_csv = ','.join(map(str, lista_datos))

                if nueva_linea_csv in [','.join(map(str, linea)) for linea in lineas]:
                    print("La línea ya existe en el archivo CSV. No se ha añadido.")
                else:
                    archivo.write("\n")
                    archivo.write(nueva_linea_csv)
        else:
            with open(ruta_de_csv, 'w', encoding= "utf-8") as file:
                claves =[
                    "Nombre",
                    "Posicion",
                    "Temporadas",
                    "Puntos totales",
                    "Promedio puntos por partido",
                    "Rebotes totales",
                    "Promedio rebotes por partido",
                    "Asistencias totales",
                    "Promedio asistencias por partido",
                    "Robos totales",
                    "Bloqueos totales",
                    "Porcentaje tiros de campo",
                    "Porcentaje tiros libres",
                    "Porcentaje tiros triples"]
                titulos = ','.join(map(str, claves))
                file.write(titulos)
                file.write("\n")
                nueva_linea_csv = ','.join(map(str, lista_datos))
            
                file.write(nueva_linea_csv)
    #4
    def seleccionar_jugador_y_mostrar_sus_logros (self):
        patron = "[a-zA-Z ]+$"
        jugador_seleccionado = input("Ingrese el nombre del jugador que desea elegir: ")

              
        
        
    
            
        
if __name__ == "__main__":             
    dream_team = Equipo(ruta_de_archivo)
    #dream_team.mostrar_todos_los_jugadores_y_su_posicion() #1
    #dream_team.seleccionar_jugador_y_mostrar_sus_estadisticas() #2 y 3
    dream_team.seleccionar_jugador_y_mostrar_sus_logros()
    


