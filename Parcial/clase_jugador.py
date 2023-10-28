from clase_equipo import Equipo

class Jugador(Equipo):
    def __init__(self, archivo, lista_de_jugadores, nombre, posicion, lista_de_logros):
        super().__init__(archivo, lista_de_jugadores)
        self.nombre = nombre
        self.posicion = posicion
        self.lista_de_logros = lista_de_logros
    