"""
1. Escribir una función que reciba un string y devuelva el mismo string todo en mayúsculas.
"""
string_a_mayusculas = lambda cadena: cadena.upper()


"""
2. Escribir una función que reciba un string y devuelva el mismo string todo en minúsculas.
"""
string_a_minisculas = lambda cadena: cadena.lower()

#print(string_a_mayusculas("MUNDO"))

"""
3. Escribir una función que tome dos strings y devuelva un nuevo string que contenga ambos strings concatenados, separados por un espacio.
"""
strings_concatenados = lambda cadena_1, cadena_2 : f"{cadena_1} {cadena_2}"

#print(strings_concatenados("Playco" , "Armboy"))

"""
4. Escribir una función que tome un string y devuelva el número de caracteres que tiene el string.
"""
numero_de_caracteres_string = lambda cadena : len(cadena)

#print(numero_de_caracteres_string("agropecuario"))

"""
5. Escribir una función que tome un string y un carácter y devuelva el número de veces que aparece ese carácter en el string.
"""
contar_caracter_en_string = lambda cadena , caracter : cadena.count(caracter)

#print(contar_caracter_en_string("atalaya" , "a"))

"""
6. Escribir una función que tome un string y un carácter y devuelva una lista con todas las palabras en el string que contienen ese carácter.
"""


"""
7. Escribir una función que tome un string y devuelva el mismo string con los espacios eliminados
"""
eliminar_espacios_string = lambda cadena : cadena.strip()

#print(eliminar_espacios_string ("      Buenas       "))
"""
8. Escribir una función que reciba dos string (nombre y apellido) y devuelva un diccionario 
con el nombre y apellido, eliminando los espacios del comienzo y el final y colocando la primer letra en mayúscula
"""
def crear_un_diccionario_a_partir_de_dos_strings (nombre : str , apellido : str) -> dict:
    diccionario_personas = {}
    nombre = nombre.strip().capitalize()
    apellido = apellido.strip().capitalize()
    mensaje = f"{nombre} {apellido}"
    
    diccionario_personas.update({"nombre y apellido" : mensaje})
    return diccionario_personas

#print(crear_un_diccionario_a_partir_de_dos_strings("    leon  " , "      sokolowski       "))

"""
9. Escribir una función que tome una lista de nombres y los una en una sola cadena separada por un
salto de línea, por ejemplo: ["Juan", "María", "Pedro"] -> "Juan\nMaría\nPedro".
"""
lista_de_nombres = ["Juan", "María", "Pedro"]
cadena = "\n"
cadena_con_saltos = lambda lista : cadena.join(lista)

#print(cadena_con_saltos(lista_de_nombres))


"""
10. Escribir una función que tome un nombre y un apellido y devuelva un email en formato "inicial_nombre.apellido@utn-fra.com.ar".
"""
gmail_persona = lambda nombre , apellido : f"{nombre[0]}.{apellido}@utn-fra.com.ar".lower()

#print(gmail_persona("León" , "Sokolowski"))

"""
11. Escribir una función que tome una lista de palabras y devuelva un string que contenga todas las 
palabras concatenadas con comas y "y" antes de la última palabra. Por ejemplo, si la lista es 
["manzanas", "naranjas", "bananas"], el string resultante debería ser "manzanas, naranjas y bananas"..
"""
lista_frutas = ["manzanas", "naranjas", "bananas" , "peras" , "frutillas"]
def enumerar_lista (lista_palabras : list) -> str:
    
    cadena = " y "
    cadena = cadena.join(lista_palabras)
    repeticion_de_y = cadena.count(" y ")
    cadena = cadena.replace(" y " , ", ", repeticion_de_y - 1)
    return cadena

#print(enumerar_lista(lista_frutas))
    

"""
12. Escribir una función que tome un número de tarjeta de crédito como input, verificar que todos los
caracteres sean numéricos y devolver los últimos cuatro dígitos y los primeros dígitos como asteriscos, 
por ejemplo: "**** **** **** 1234". 
"""
def tomar_numero_de_tarjeta () -> str:
    numero_tarjeta = input("Ingrese el número de su tarjeta: ")

"""
13. Escribir una función que tome un correo electrónico y elimine cualquier carácter después del símbolo @, 
por ejemplo: "usuario@gmail.com" -> "usuario".
"""

"""
14. Escribir una función que tome una URL y devuelva solo el nombre de dominio, por ejemplo: 
"https://www.ejemplo.com.ar/pagina1" -> "ejemplo"..
"""

"""
15. Escribir una función que tome una cadena de texto y devuelva solo los caracteres alfabéticos, eliminando
cualquier número o símbolo (sólo son válidos letras y espacios), por ejemplo: "H0l4, m4nd0!" -> "Hl mnd”
"""

"""
16. Escribir una función que tome una cadena de texto y la convierta en un acrónimo, tomando la primera letra
de cada palabra, por ejemplo: "Universidad Tecnológica Nacional Facultad Regional Avellaneda" -> "UTNFRA”.
"""

"""
17. Escribir una función que tome un número binario y lo convierta en una cadena de 8 bits, rellenando con ceros
a la izquierda si es necesario, por ejemplo: "101" -> "00000101".
"""

"""
18. Escribir una función que tome una cadena de caracteres y reemplace todas las letras mayúsculas por letras
minúsculas y todas las letras minúsculas por letras mayúsculas, por ejemplo: "HoLa" -> "hOlA"
"""

"""
19. Escribir una función que tome una cadena de caracteres y cuente la cantidad de dígitos que contiene, 
por ejemplo: "1234 Hola Mundo" -> contiene 4 dígitos.
"""

"""
20. Escribir una función que tome una lista de direcciones de correo electrónico y las una en una sola cadena
separada por punto y coma, por ejemplo: ["juan@gmail.com", "maria@hotmail.com"] -> "juan@gmail.com;maria@hotmail.com".
"""

"""
21. Crear una función que reciba como parámetro un string y devuelva un diccionario donde cada clave 
es una palabra y cada valor es un entero que indica cuántas veces aparece esa palabra dentro del string.
"""

