class Estadisticas():
    def __init__(self, diccionario_estadisticas : dict) -> None: 
        self.__temporadas = diccionario_estadisticas.get("temporadas")
        self.__puntos_totales = diccionario_estadisticas.get("puntos_totales")
        self.__promedio_puntos_x_partido = diccionario_estadisticas.get("promedio_puntos_por_partido")
        self.__rebotes_totales = diccionario_estadisticas.get("rebotes_totales")
        self.__promedio_rebotes_x_partido = diccionario_estadisticas.get("promedio_rebotes_por_partido")
        self.__asistencias_totales = diccionario_estadisticas.get("asistencias_totales")
        self.__promedio_asistencias_x_partido = diccionario_estadisticas.get("promedio_asistencias_por_partido")
        self.__robos_totales = diccionario_estadisticas.get("robos_totales")
        self.__bloqueos_totales = diccionario_estadisticas.get("bloqueos_totales")
        self.__porcentaje_tiros_de_2 = diccionario_estadisticas.get("porcentaje_tiros_de_campo")
        self.__porcentaje_libres = diccionario_estadisticas.get("porcentaje_tiros_libres")
        self.__porcentaje_triples = diccionario_estadisticas.get("porcentaje_tiros_triples")
        self.__claves_de_estadisticas = list(diccionario_estadisticas.keys())
        self.__valores_de_estadisticas = list(diccionario_estadisticas.values())
    
    @property
    def obtener_temporadas (self):
        """
        Devuelve: el valor del atributo.
        """
        return self.__temporadas
    
    @property
    def obtener_puntos_totales (self):
        """
        Devuelve: el valor del atributo.
        """
        return self.__puntos_totales
    
    @property
    def obtener_promedio_puntos_x_partido (self):
        """
        Devuelve: el valor del atributo.
        """
        return self.__promedio_puntos_x_partido
    
    @property
    def obtener_rebotes_totales (self):
        """
        Devuelve: el valor del atributo.
        """
        return self.__rebotes_totales
    
    @property
    def obtener_promedio_rebotes_x_partido (self):
        """
        Devuelve: el valor del atributo.
        """
        return self.__promedio_rebotes_x_partido
    
    @property
    def obtener_asistencias_totales (self):
        """
        Devuelve: el valor del atributo.
        """
        return self.__asistencias_totales
    
    @property
    def obtener_promedio_asistencias_x_partido (self):
        """
        Devuelve: el valor del atributo.
        """
        return self.__promedio_asistencias_x_partido
    
    @property
    def obtener_robos_totales (self):
        """
        Devuelve: el valor del atributo.
        """
        return self.__robos_totales
    
    @property
    def obtener_bloqueos_totales (self):
        """
        Devuelve: el valor del atributo.
        """
        return self.__bloqueos_totales
    
    @property
    def obtener_porcentaje_tiros_de_2 (self):
        """
        Devuelve: el valor del atributo.
        """
        return self.__porcentaje_tiros_de_2
    
    @property
    def obtener_porcentaje_libres (self):
        """
        Devuelve: el valor del atributo.
        """
        return self.__porcentaje_libres
    
    @property
    def obtener_porcentaje_triples (self):
        """
        Devuelve: el valor del atributo.
        """
        return self.__porcentaje_triples
    
    @property
    def obtener_claves_de_estadisticas(self):
        """
        Devuelve: el valor del atributo.
        """
        return self.__claves_de_estadisticas
    
    @property
    def obtener_valores_de_estadisticas(self):
        """
        Devuelve: el valor del atributo.
        """
        return self.__valores_de_estadisticas
    


    