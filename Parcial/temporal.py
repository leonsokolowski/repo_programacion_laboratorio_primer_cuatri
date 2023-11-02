import re
lista = ["1", "0", "11", "13", "20", "14", "a"]

patron = "[1-9]+"
for palabra in lista:
    if re.match(patron, palabra):
        print(palabra)