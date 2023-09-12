"""
7. Crear una función que calcule el máximo común divisor de dos números. Recibe dos parámetros (números) y devuelve el máximo común divisor.
"""
# def calcular_mcd(num1, num2):
#     while num2:
#         num1, num2 = num2, num1 % num2
#     return num1

# num1 = 48
# num2 = 18

# mcd = calcular_mcd(num1, num2)

# print(f"El MCD de {num1} y {num2} es {mcd}")


# a = 48
# b = 18

def calcular_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

resto = 48 % 18
print(resto)

