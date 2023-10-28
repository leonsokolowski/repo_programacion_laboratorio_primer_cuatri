import json
class Equipo:
    def __init__(self, archivo, lista_de_jugadores):
        self.archivo = archivo
        self.lista_de_jugadores = lista_de_jugadores
    
    def importar_json (self):
        with open(self.archivo, "r", encoding= "utf-8") as jugadores_dream_team:
            objeto = json.load(jugadores_dream_team)
            return objeto
    
    
             
dream_team = Equipo("Parcial/dream_team.json", [])
print (dream_team.importar_json())
