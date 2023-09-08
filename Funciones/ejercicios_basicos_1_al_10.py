"""
10 Crea una función que reciba como parámetros una lista de palabras y devuelva la palabra más larga.
"""

lista_de_palabras = ["agua" , "elefante" , "traumatología" , "onomatopeya"]

def encuentra_palabra_mas_larga_de_la_lista (lista_palabras):
    
    palabra_mas_larga = None
    
    for palabra in lista_palabras:
        
        if palabra_mas_larga == None or len(palabra_mas_larga) < len(palabra):
            palabra_mas_larga = palabra
    
    return palabra_mas_larga

palabra_encontrada = encuentra_palabra_mas_larga_de_la_lista (lista_de_palabras)
print (f"La palabra más larga es: {palabra_encontrada}")
        
    