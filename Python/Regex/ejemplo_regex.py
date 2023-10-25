import re

texto = [
    "NATHY PELUSO || BZRP Music Sessions#36",
    "NATHY PELUSO || BZRP Music Sessions#37",
    "NATHY PELUSO || BZRP Music Sessions%36",
    "NATHY PELUSO || BZRP Music Sessions&&36",
    "NATHY PELUSO || BZRP Music Sessions#40",
    ]
 
patron_de_busqueda = "(^[a-zA-Z ]+$)"

nombre = ""
while not re.match(patron_de_busqueda, nombre):
    nombre = input("Escriba su nombre: ")
print(nombre)
    
    
#for titulo in texto:
    
    
    #print()