import re
lista = ["archivo_hola", "ARCHIVO", "Archivo Json Parcial", "!archivo", "_________"]

patron = "([a-zA-Z0-9_ ]+$)"
for palabra in lista:
    if re.match(patron, palabra):
        print(palabra)