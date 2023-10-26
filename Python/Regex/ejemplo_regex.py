import re

textos = [
    "NATHY PELUSO || BZRP Music Sessions#36",
    "NATHY PELUSO || BZRP Music Sessions#37",
    "NATHY PELUSO || BZRP Music Sessions%36",
    "NATHY PELUSO || BZRP Music Sessions&&36",
    "NATHY PELUSO || BZRP Music Sessions#40"
    ]
 
patron_de_busqueda = "^[a-zA-Z ]+\|\|[a-zA-Z ]+#[0-9]{2}$"

for texto in textos:
    if re.match(patron_de_busqueda, texto):
        print(texto)
        
# nombre = ""
# while not re.match(patron_de_busqueda, nombre):
#     nombre = input("Escriba su nombre: ")
# print(nombre)
    
    
#for titulo in texto:
    
    
    #print()