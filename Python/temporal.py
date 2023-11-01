# import re
# """
# nombres = [
#     "Michael Jordan",
#     "Kobe Bryant",
#     "Manu Ginobili",
#     "452",
#     "Pepe",
#     "Kokorito525"
#     ]

# patron = "[a-zA-Z ]+$"

# for nombre in nombres:
#     if re.match(patron, nombre):
#         print(nombre)
#     else: 
#         print("caca")
# """        
        
# indices = [
#     "1",
#     "2",
#     "3",
#     "4",
#     "5",
#     "6",
#     "7",
#     "8",
#     "9",
#     "10",
#     "11",
#     "12",
#     "13",
#     "14",
# ]

# patron = "[0-9]|[0-9]{2}"

# for indice in indices:
#     if re.match(patron, indice):
#         indice = int(indice)
#         if indice <= 12:
#             print(indice)
#         elif indice <= 0:
#             print("No existe ese indice")
#         else:
#             print("No existe ese indice")

numero = 0

for i in range (10):
    numero += 1
    print(numero)
    
    
# def crear_csv(self, lista, indice: int, ejercicio_3 : bool):
#         """
#         Consigue todos los datos que va a importar al CSV.
#         Si el archivo CSV existe, lo lee linea por linea.
#         En caso de que la linea que se quiere importar ya exista, no se importa, si no existe, la crea.
#         Si el archivo CSV no existe, lo crea, crea una primera linea con los nombres de los datos que luego agregara.
#         Recibe: self y un dato int.
#         Devuelve: nada.
#         """
        
#         lista_datos = []
#         ruta = ""
#         if ejercicio_3:
#             ruta = ruta_de_csv
#             nombre = lista[indice].obtener_nombre_jugador
#             lista_datos.append(nombre)
#             posicion = lista[indice].obtener_posicion_jugador
#             lista_datos.append(posicion)
#             estadisticas = lista[indice].obtener_estadisticas_completas()
#             for v in estadisticas.values():
#                 lista_datos.append(v)
        
#         else:
#             ruta = r"Parcial\Sokolowski.csv"
#             nombre = lista[indice].obtener_nombre_jugador
#             lista_datos.append(nombre)
#             temporadas = lista[indice].obtener_estadisticas_completas()['temporadas']
#             lista_datos.append(temporadas)
            

#         if os.path.isfile(ruta):
#             with open(ruta, 'r+', newline='') as archivo:
#                 lector_csv = csv.reader(archivo)
#                 lineas = list(lector_csv)
#                 nueva_linea_csv = ','.join(map(str, lista_datos))

#                 if ejercicio_3:
#                     if nueva_linea_csv in [','.join(map(str, linea)) for linea in lineas]:
#                         print("La línea ya existe en el archivo CSV. No se ha añadido.")
#                     else:
#                         archivo.write("\n")
#                         archivo.write(nueva_linea_csv)
#                 else:
#                     archivo.write("\n")
#                     archivo.write(nueva_linea_csv)
#         else:
#             with open(ruta, 'w', encoding= "utf-8") as file:
#                 if ejercicio_3:
#                     claves =[
#                         "Nombre",
#                         "Posicion",
#                         "Temporadas",
#                         "Puntos totales",
#                         "Promedio puntos por partido",
#                         "Rebotes totales",
#                         "Promedio rebotes por partido",
#                         "Asistencias totales",
#                         "Promedio asistencias por partido",
#                         "Robos totales",
#                         "Bloqueos totales",
#                         "Porcentaje tiros de campo",
#                         "Porcentaje tiros libres",
#                         "Porcentaje tiros triples"]
#                 else:
#                     claves =[
#                         "Nombre",
#                         "Temporadas"
#                     ]
#                 titulos = ','.join(map(str, claves))
#                 file.write(titulos)
#                 file.write("\n")
#                 nueva_linea_csv = ','.join(map(str, lista_datos))
            
#                 file.write(nueva_linea_csv)

