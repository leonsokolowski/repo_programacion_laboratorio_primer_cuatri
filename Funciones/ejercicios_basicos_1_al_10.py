"""
León Sokolowski
León Sokolowski
División H
Grupo Alpha
"""
"""
1. Crear una función que convierta grados Celsius a grados Fahrenheit. 
Recibe un parámetro (grados Celsius) y devuelve el resultado en grados Fahrenheit.
"""
def conversor_grados_celcius_a_fahrenheit (grados_celsius : float) -> float:
    """
    Convierte el numero flotante que representa grados Celsius a grados Fahrenheit.
    Recibe : un dato flotante.
    Devuelve : un dato flotante.
    """

    grados_fahrenheit = (grados_celsius * 9/5) + 32
    return grados_fahrenheit

print(conversor_grados_celcius_a_fahrenheit(22)) #22° Celsius de ejemplo

"""
2. Crear una función que calcule el área de un círculo. Recibe un parámetro (radio) y devuelve el área del círculo.
"""
def calcula_area_de_un_circulo (radio : float) -> float:
    """
    Calcula el area de un circulo usando el radio del mismo.
    Recibe : un dato flotante.
    Devuelve : un dato flotante.
    """
    
    area_circulo = 3.14 * (radio**2)
    return area_circulo

print(calcula_area_de_un_circulo(5))

"""
3. Crear una función que calcule el descuento aplicado a un producto. 
Recibe dos parámetros (precio original y precio con descuento) y devuelve el porcentaje de descuento aplicado.
"""
def calcular_descuento_porcentual (precio_original : float , precio_con_descuento : float) -> float:
    """
    Calcula el porcentaje que hará que el precio original termine siendo el precio con descuento.
    Recibe: Dos datos flotantes, el precio original y el precio con descuento.
    Devuelve: Un dato flotante, el porcentaje de descuento.
    """
    descuento_porcentual =  100 - (precio_con_descuento / precio_original) * 100
    return descuento_porcentual

print(f"Descuento porcentual: {calcular_descuento_porcentual(100,80)}%")

"""
4. Crear una función que calcule el promedio de edad de un grupo de personas. Recibe una lista de edades y devuelve el promedio.
"""
def calcula_promedio_edades (lista_edades: list[int]) -> float:
    """
    Recorre una lista de datos enteros y realiza un promedio de ellos.
    Recibe: una lista.
    Devuelve: un dato flotante.
    """    
    cantidad_edades = len(lista_edades)
    acumulador_edades = 0
    
    for edad in lista_edades:
        acumulador_edades += edad
    
    promedio_edades = acumulador_edades / cantidad_edades
    return promedio_edades

"""
5. Crear una función que determine si un número es primo o no. Recibe un parámetro (número) y devuelve True si es primo y False si no lo es.
"""
def determina_si_numeros_primo_o_no (numero : int) -> bool:
    """
    Determina mediante el uso de operador de módulo si un numero es primo o no.
    Recibe: Un dato entero.
    Devuelve: Un dato booleano.
    """    
    contador = 1
    divisores_de_numero = 0
    
    while contador <= numero:
        if numero % contador == 0:
            divisores_de_numero += 1
        contador += 1
    
    if divisores_de_numero == 2:
        dato_final = True
    else:
        dato_final = False
    
    return dato_final
            
print(determina_si_numeros_primo_o_no(7))
print(determina_si_numeros_primo_o_no(8))

"""
6. Crear una función que calcule el área de un triángulo. Recibe dos parámetros (base y altura) y devuelve el área.
"""
def calcula_area_triangulo (base : float , altura : float) -> float:
    """
    Calcula el area de un triángulo mediante la formula correspondiente.
    Recibe: dos datos flotantes, la base del triángulo y la altura.
    Devuelve: un dato flotante, el area del triángulo.
    """
    area_triangulo = (base * altura) / 2
    
    return area_triangulo

"""
7. Crear una función que calcule el máximo común divisor de dos números. Recibe dos parámetros (números) y devuelve el máximo común divisor.
"""


"""
8. Crear una función que verifique si un número es par o impar. Recibe un número como parámetro y devuelve True si es par o False si es impar.
"""
def verifica_si_numero_par_o_no (numero : int) -> bool:
    """
    Verifica si un número es par o no dividiendolo por 2.
    Recibe: un dato entero.
    Devuelve: un dato booleano.
    """
    if numero % 2 == 0:
        dato_final = True
    else:
        dato_final = False
    
    return dato_final

"""
9. Crear una función que cuente la cantidad de veces que aparece un elemento en una lista. 
Recibe una lista y un elemento como parámetros y devuelve la cantidad de veces que aparece en la lista.
"""
lista_de_numeros = [ 8, 56, 8, 8, 9, 32, 44, 8 ]

def cuenta_cantidad_de_veces_que_elemento_aparece_en_lista (lista_numeros : list[int], elemento : int) -> int:
    
    contador_veces_de_aparicion = 0
    
    for i in lista_numeros:
        if i == elemento:
            contador_veces_de_aparicion += 1
    
    return contador_veces_de_aparicion

print(cuenta_cantidad_de_veces_que_elemento_aparece_en_lista(lista_de_numeros, 8))

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
        
    