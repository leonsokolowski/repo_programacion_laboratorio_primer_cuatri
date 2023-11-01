from clase_estadísticas import Estadisticas
class Jugador():
    def __init__(self, diccionario_jugador : dict) -> None:
        self.__nombre_jugador = diccionario_jugador.get("nombre")
        self.__posicion_jugador = diccionario_jugador.get("posicion")
        self.__logros_jugador = diccionario_jugador.get("logros")
        self.__estadisticas_jugador = Estadisticas(diccionario_jugador.get("estadisticas"))
        self.estadisticas_completas = self.obtener_estadisticas_completas()
    @property
    def obtener_nombre_jugador (self) -> str:
        """
        Devuelve: el valor del atributo.
        """
        return self.__nombre_jugador
    
    @property
    def obtener_posicion_jugador (self) -> str:
        """
        Devuelve: el valor del atributo.
        """
        return self.__posicion_jugador
    
    @property
    def obtener_estadisticas_jugador (self) -> object:
        """
        Devuelve: el valor del atributo.
        """
        return self.__estadisticas_jugador
    
    @property
    def obtener_logros_jugador (self) -> list[str]:
        """
        Devuelve: el valor del atributo.
        """
        return self.__logros_jugador
    
    def obtener_estadisticas_completas(self) -> dict:
        """
        Crea un diccionario con las estadisticas del jugador.
        Recibe: self.
        Devuelve: un diccionario.
        """
        cantidad_de_estadisticas = len(self.obtener_estadisticas_jugador.obtener_claves_de_estadisticas)
        estadisticas_completas = {}
        for i in range (cantidad_de_estadisticas):
            estadisticas_completas.update({self.obtener_estadisticas_jugador.obtener_claves_de_estadisticas[i] : self.obtener_estadisticas_jugador.obtener_valores_de_estadisticas[i]}) 
        return estadisticas_completas
    
        
               
    