import json
class Equipo:
    def __init__(self, archivo, lista_de_jugadores):
        self.archivo = archivo
        self.lista_de_jugadores = lista_de_jugadores
    
    def importar_json (self, clave):
        with open(self.archivo, "r", encoding= "utf-8") as jugadores_dream_team:
            objeto = json.load(jugadores_dream_team)
            jugadores = objeto.get(clave)
            for jugador in jugadores:
                self.lista_de_jugadores.append(jugador)
            return self.lista_de_jugadores
        
             
dream_team = Equipo("Parcial/dream_team.json", [])
print (dream_team.importar_json("jugadores"))


