# def imprimir_menu ():
#     """
#     Imprime un menu.
#     Recibe: nada.
#     Devuelve: nada.
#     """
#     menu = \
#     """
#     1. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe.
#     2. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo .
#     3. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO).
#     4. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO).
#     5. Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO).
#     6. Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO).
#     7. Calcular e informar cual es el superhéroe más y menos pesado.
#     8. Salir.
#     """
#     print(menu)

lista_flotantes = [-6.0, -3.0, 1.0, 4.0, 6.0, 7.0, 8.0, 9.0]

def quick_sort (lista : list[float]):
    
    if len(lista) < 2:
        return lista
    else:
        lista_a_ordenar = lista.copy()
        pivot = lista_a_ordenar.pop(0)
        numeros_mas_grandes = []
        numeros_mas_chicos = []
        
        for numero in lista_a_ordenar:
            if numero > pivot:
                numeros_mas_grandes.append(numero)
            elif numero <= pivot:
                numeros_mas_chicos.append(numero)
        
    return quick_sort(numeros_mas_grandes) + [pivot] + quick_sort(numeros_mas_chicos)

print(quick_sort(lista_flotantes))

