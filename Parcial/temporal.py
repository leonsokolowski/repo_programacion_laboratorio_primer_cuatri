"""
import json
ruta_de_acceso = "Parcial/dream_team.json"
with open(ruta_de_acceso, "r", encoding= "utf-8") as miarchivo:
    objeto = json.load(miarchivo)
    print(objeto)
    
    
def importar_json (archivo):
        with open(archivo, "r", encoding= "utf-8") as jugadores_dream_team:
            objeto = json.load(jugadores_dream_team)
            return objeto

print(importar_json(ruta_de_acceso))
"""

# class Persona():
#     def __init__ (self, nombre, apellido, edad, dni):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.dni = dni
    
#     def presentarse (self):
#         print(f"Hola me llamo {self.nombre} {self.apellido}")

# chechu = Persona("Cecilia", "Woitasen", 26, 40073938)

# class Alumno(Persona):
#     pass

