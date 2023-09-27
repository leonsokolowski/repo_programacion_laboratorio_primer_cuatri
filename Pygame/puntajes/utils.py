def formatear_puntaje(puntaje: str) -> str:
    puntaje = puntaje.zfill(5)
    return puntaje

def formatear_nombre_jugador(nombre: str) -> str:
    nombre = nombre.upper()
    
    nombre = nombre.strip()
    
    nombre = nombre[0:" "]
    
    return nombre
