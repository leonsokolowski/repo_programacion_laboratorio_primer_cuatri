import re
#re.match: Busca un patrón dentro de un string.
textos = [
    "NATHY PELUSO || BZRP Music Sessions#36",
    "NATHY PELUSO || BZRP Music Sessions#37",
    "NATHY PELUSO || BZRP Music Sessions%36",
    "NATHY PELUSO || BZRP Music Sessions&&36",
    "NATHY PELUSO || BZRP Music Sessions#40"
    ]
 
patron_de_busqueda = "^[a-zA-Z ]+\|\|[a-zA-Z ]+#[0-9]{2}$"
                    #"^[a-zA-Z ]+\|\|[a-zA-Z ]+#[0-9]+$"
                    #"^[a-zA-Z ]+\|\|[a-zA-Z ]+#[0-9]{1,2}$"

for texto in textos:
    if re.match(patron_de_busqueda, texto):
        print(texto)
    
# nombre = ""
# while not re.match(patron_de_busqueda, nombre):
#     nombre = input("Escriba su nombre: ")
# print(nombre)

fechas = [
    "2023/09/28 10:00:00 PM",
    "2023/09/30 20:30:15", 
    "2023/09/28 10:00:00 AM",
    "2023/09/28 99:90:99"
]
"""
patron_de_busqueda_fecha = "(^[0-9]{4}\/[0-9]{2}\/[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}$)"
                           "(^[0-9]{4}\/[0-9]{2}\/[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}) (AM|PM)$"
                           "(^[\d]{4}\/[\d]{2}\/[\d]{2} [\d]{2}:[\d]{2}:[\d]{2}$)"
"""
patron_de_fecha = "([0-9]{4}\/[0-9]{2}\/[0-9]{2})"
patron_de_hora = "([0-9]{2}:[0-9]{2}:[0-9]{2})"
patron_de_tiempo = "(AM|PM)"
patron_completo = f"^{patron_de_fecha} {patron_de_hora} {patron_de_tiempo}$"
"""
for fecha in fechas:
    if re.match(patron_completo,fecha):
        print(fecha)
"""
#------------------------------------------------------------------------------------------------------------------------------------------        
#re.split: retorna una lista que contiene la cadena que decidimos dividir por el parametro que desarrollamos.
"""
texto = "uno 1 dos 2 tres 3 cuatro"
patron = " [0-9]{1} "
print(re.split(patron, texto))
"""
"""
texto = "uno 1 dos 2 tres 3 cuatro # cinco ! seis"
#patron = " [0-9]{1} | [^\d] "
patron = " [^a-z]{1} "
print(re.split(patron, texto))
"""
# jdsajd
# daskjldhsakldhlsa
# dklsajdklsaj
# dhdas+da