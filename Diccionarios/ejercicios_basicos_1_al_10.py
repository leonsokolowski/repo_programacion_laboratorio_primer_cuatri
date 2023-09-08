"""
León Sokolowski
León Sokolowski
División H
Grupo Alpha
"""

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
5. Crea un diccionario que represente los continentes, donde las claves son los nombres de los continentes y 
los valores son los números correspondientes (por ejemplo, {"América": 1, "Europa": 2, ...}). 
Imprime el valor correspondiente al continente "África".
"""
continentes_del_mundo = {
    "Asia" : 1,
    "America" : 2,
    "Africa" : 3,
    "Europa" : 4,
    "Oceania" : 5,
    "Antartida" : 6
}

valor_continente_seleccionado = continentes_del_mundo.get("Africa", "Ese continente no existe")
print (f"El valor de Africa es {valor_continente_seleccionado}")

"""
6. Crea un diccionario que represente las estaciones del año, donde las claves son los nombres de las estaciones y 
los valores son los números correspondientes (por ejemplo, {"primavera": 1, "verano": 2, ...}). 
Imprime el valor correspondiente a la estación "invierno".
"""
estaciones_del_año = {
    "verano" : 1,
    "otoño" : 2,
    "invierno" : 3,
    "primavera" : 4
}

valor_estacion_seleccionada = estaciones_del_año.get("invierno" , "No existe esa estación del año")

print(f"El valor de invierno es {valor_estacion_seleccionada}")

"""
7. Crea un diccionario que contenga la información de una canción: título, artista y duración. Luego, imprime la duración de la canción.
"""
info_cancion = {
    "titulo" : "Heart to Heart",
    "artista" : "Mac DeMarco",
    "duracion" : 3.31
}

valor_info_seleccionada = info_cancion.get("duracion", "No poseemos esa información")
print(f"La duración de la canción es de {valor_info_seleccionada}")

"""
8. Crea un diccionario que represente las edades de varias personas, donde las claves son los nombres de las personas
y los valores son sus edades. Imprime la edad de la persona más joven.
"""
edades_personas = {
    "Benicio" : 13,
    "Wanda" : 22,
    "Julieta" : 15,
    "Leon" : 18
}

edad_persona_mas_joven = None
nombre_persona_mas_joven = None

for clave, valor in edades_personas.items():
    if edad_persona_mas_joven == None or edad_persona_mas_joven > valor:
        edad_persona_mas_joven = valor
        nombre_persona_mas_joven = clave

print(f"La persona más joven es {nombre_persona_mas_joven} con {edad_persona_mas_joven}")

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

"""
10.Crea un diccionario que represente las notas de un examen de varios estudiantes, donde las claves son los nombres de 
los estudiantes y los valores son sus notas. Imprime el promedio de las notas.
"""
notas_estudiantes = {
    "Tani" : 9,
    "Z" : 8,
    "Marce" : 7,
    "León" : 10
}
acumulador_notas = 0
contador_notas = 0
for claves, valor in notas_estudiantes.items():
    acumulador_notas += valor
    contador_notas += 1

promedio_notas = acumulador_notas / contador_notas

print (f"El promedio de las notas de los alumnos es de {promedio_notas}")