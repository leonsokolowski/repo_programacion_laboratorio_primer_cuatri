"""
1. Crea un diccionario que represente los días de la semana, donde las claves son los nombres de los días
y los valores son los números correspondientes (por ejemplo, {"lunes": 1, "martes": 2, ...}).
Imprime el valor correspondiente al día "miércoles".

"""

# dias_de_la_semana = {}

# dias_de_la_semana ["lunes"] = 1
# dias_de_la_semana ["martes"] = 2
# dias_de_la_semana ["miecoles"] = 3
# dias_de_la_semana ["jueves"] = 4
# dias_de_la_semana ["viernes"] = 5
# dias_de_la_semana ["sabados"] = 6
# dias_de_la_semana ["domingo"] = 7

#dias_de_la_semana ["miecoles"] = 48 --> Si se escribe la misma clave con un distinto elemento se va a reemplazar.

dias_de_la_semana = {
    "lunes" : 1,
    "martes" : 2,
    "miercoles" : 3,
    "jueves" : 4,
    "viernes" : 5,
    "sabado" : 6,
    "domingo" : 7   
}

# #print (dias_de_la_semana ["miercoles"]) --> funciona

print (dias_de_la_semana.get("miercoles", "No se encontró la clave"))
# #.get es un metodo. Los metodos siempre llevan ()

"""
2. Crea un diccionario que represente los meses del año, donde las claves son los nombres de los meses y los valores son sus números
correspondientes (por ejemplo, {"enero": 1, "febrero": 2, ...}). Imprime el número correspondiente al mes "julio"..

"""

meses_del_anho = {
    "enero" : 1,
    "febrero" : 2,
    "marzo" : 3,
    "abril" : 4,
    "mayo" : 5,
    "junio" : 6,
    "julio" : 7,
    "agosto" : 8,
    "septiembre" : 9,
    "octubre" : 10,
    "noviembre" : 11,
    "diciembre" : 12
}

print (meses_del_anho.get("julio", "No se encontró la clave"))

"""
3. Crea un diccionario que contenga la información de una película, como título, director y año de estreno. Luego, imprime el título de la película.

"""

info_pelicula = {
    "titulo" : "The batman",
    "director" : "Matt Reaves",
    "año" : 2022
}

print (info_pelicula.get("titulo", "No se encontró la clave"))

"""
4. Crea un diccionario que contenga la información de una dirección: nombre de la calle, altura, localidad, 
código postal, partido y provincia. Luego, imprime el nombre de la calle, seguido de su altura.

"""

info_direccion = {
    "nombre_calle" : "Calle Wallaby",
    "altura" : 42,
    "localidad" : "P Sherman",
    "partido" : "Sidney",
    "codigo postal" : 7832,
    "provincia" : "Dory" 
}

nombre_calle = info_direccion.get("nombre_calle", "El nombre de la calle no fue definido.")
altura = info_direccion.get("altura", "La altura de la calle no fue definida.")

print (f"Calle: {nombre_calle}\nAltura: {altura}") 

"""
9. Crea un diccionario que contenga las capitales de los países de América del Sur. 
Luego, pide al usuario que ingrese el nombre de un país y muestra su capital correspondiente.

"""

capitales_america_del_sur = {
    "Argentina" : "Buenos Aires",
    "Brasil" : "Brasilia",
    "Uruguay" : "Montevideo",
    "Paraguay" : "Asuncion",
    "Bolivia" : "La paz"
}

pais_seleccionado = input("Ingrese un país de América del Sur:").capitalize() 
#.capitalize() pone todas las letras de una palabra en minúsculas y solo la primera en mayúscula

# if not pais_seleccionado in capitales_america_del_sur.keys():
#     mensaje = "Ese país no existe o no pertenece a América del Sur"
# else:
#     capital_correspondiente = capitales_america_del_sur.get(pais_seleccionado)
#     mensaje = f"La capital de {pais_seleccionado} es {capital_correspondiente}!"

while not pais_seleccionado in capitales_america_del_sur.keys():
    mensaje = f"El país {pais_seleccionado} no existe o no está en AdS, ingrese otro:"
    pais_seleccionado = input(mensaje).capitalize()
else:
    capital_correspondiente = capitales_america_del_sur.get(pais_seleccionado)
    mensaje = f"La capital de {pais_seleccionado} es {capital_correspondiente}!"

print (mensaje)

