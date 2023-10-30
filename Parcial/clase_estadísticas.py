class Estadisticas():
    def __init__(self, diccionario_estadisticas : dict) -> None: 
        self.temporadas = diccionario_estadisticas.get("temporadas")
        self.puntos_totales = diccionario_estadisticas.get("puntos_totales")
        self.promedio_puntos_x_partido = diccionario_estadisticas.get("promedio_puntos_por_partido")
        self.rebotes_totales = diccionario_estadisticas.get("rebotes_totales")
        self.promedio_rebotes_x_partido = diccionario_estadisticas.get("promedio_rebotes_por_partido")
        self.asistencias_totales= diccionario_estadisticas.get("asistencias_totales")
        self.promedio_asistencias_x_partido = diccionario_estadisticas.get("promedio_asistencias_por_partido")
        self.robos_totales = diccionario_estadisticas.get("robos_totales")
        self.bloqueos_totales = diccionario_estadisticas.get("bloqueos_totales")
        self.porcentaje_tiros_de_2 = diccionario_estadisticas.get("porcentaje_tiros_de_campo")
        self.porcentaje_libres = diccionario_estadisticas.get("porcentaje_tiros_libres")
        self.porcentaje_triples = diccionario_estadisticas.get("porcentaje_tiros_triples")
        self.claves_de_estadisticas = list(diccionario_estadisticas.keys())
        self.valores_de_estadisticas = list(diccionario_estadisticas.values())
    
    @property
    def obtener_temporadas (self):
        return self.temporadas
    
    @property
    def obtener_puntos_totales (self):
        return self.puntos_totales
    
    @property
    def obtener_puntos_x_partido (self):
        return self.obtener_puntos_x_partido
    
    @property
    def obtener_rebotes_totales (self):
        return self.rebotes_totales
    
    @property
    def obtener_promedio_rebotes_x_partido (self):
        return self.promedio_rebotes_x_partido
    
    @property
    def obtener_asistencias_totales (self):
        return self.asistencias_totales
    
    @property
    def obtener_promedio_asistencias_x_partido (self):
        return self.promedio_asistencias_x_partido
    
    @property
    def obtener_robos_totales (self):
        return self.obtener_robos_totales
    
    @property
    def obtener_bloqueos_totales (self):
        return self.bloqueos_totales
    
    @property
    def obtener_porcentaje_tiros_de_2 (self):
        return self.porcentaje_tiros_de_2
    
    @property
    def obtener_porcentaje_libres (self):
        return self.porcentaje_libres
    
    @property
    def obtener_porcentaje_triples (self):
        return self.porcentaje_triples
    
    @property
    def obtener_claves_de_estadisticas(self):
        return self.claves_de_estadisticas
    
    @property
    def obtener_valores_de_estadisticas(self):
        return self.valores_de_estadisticas
    


    