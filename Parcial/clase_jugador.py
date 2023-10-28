from clase_equipo import Equipo

class Jugador(Equipo):
    def __init__(self, archivo, nombre, posicion, lista_de_logros):
        super().__init__(archivo)