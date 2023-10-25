#Ejemplo
#Crear una lista donde cada elemento tiene el valor del doble del número de la lista de números.
"""
lista_numeros = [1, 2, 3, 4, 5]

#1era manera
lista_dobles = []
for numero in lista_numeros:
    resultado = numero * 2
    lista_dobles.append(resultado)
print(lista_dobles)

#2da manera
lista_dobles_2 = list(map(lambda numero: numero * 2, lista_numeros)) 
#El map usa una función y un iterable y a cada valor del iterable le aplica la función.
print(lista_dobles_2)
"""
#--------------------------------------------------------------------------------------------------------------
#LISTA POR COMPRENSIÓN
#Crear una lista donde cada elemento tiene el valor del doble del número de la lista de números.
lista_numeros = [1, 2, 3, 4, 5]

lista_dobles = [numero * 2 for numero in lista_numeros] #Versión simplificada sin filtro.
print(lista_dobles)

lista_dobles_filtro = [numero * 2 for numero in lista_numeros if numero > 2] #Versión con filtro
print(lista_dobles_filtro)

#Crear una lista con los nombres convertidos a minúsculas.

lista_nombres = ["María", "Juan", "Paula", "Andrés", "Julieta", "Alejandra", "Martin", "Hector", "Wanda"]

lista_nombres_minus = [nombre.lower() for nombre in lista_nombres]
print(lista_nombres_minus)