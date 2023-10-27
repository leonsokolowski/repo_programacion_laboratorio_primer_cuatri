import json
ruta_de_acceso = "1/dream_team.json"
archivo = open(ruta_de_acceso, "r", encoding= "utf-8")
for linea in archivo:
    print(linea)