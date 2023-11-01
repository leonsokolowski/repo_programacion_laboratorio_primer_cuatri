import json
import re
from clase_jugador import Jugador

ruta_de_archivo = r"Parcial\dream_team.json"
ruta_de_csv = r"Parcial\estadisticas_basquetbolistas.csv"
 
class Equipo():
    def __init__(self, archivo):
        self.archivo = archivo
        self.lista_de_jugadores = self.crear_jugadores_y_agregarlos_a_lista()
        
        
    def importar_json (self) -> dict:
        """
        Importa el archivo JSON.
        Recibe: self.
        Devuelve: un diccionario
        """
        try:
            with open(self.archivo, "r", encoding= "utf-8") as jugadores_dream_team:
                diccionario_equipo = json.load(jugadores_dream_team)
            return diccionario_equipo
        except FileNotFoundError:
            print("Error, archivo no encontrado")
        except json.JSONDecodeError:
            print("Error al decodificar el JSON")

            
    
    def crear_jugadores_y_agregarlos_a_lista (self) -> list:
        """
        Crea a cada objeto de la clase Jugador y lo agrega a una lista.
        Recibe: self.
        Devuelve: una lista de objetos.
        """
        lista_de_jugadores = []
        try:
            data_jugadores = self.importar_json().get("jugadores")
            for jugador in data_jugadores:
                lista_de_jugadores.append(Jugador(jugador))
            return lista_de_jugadores
        except:
            print("Error con el archivo")
    #1
    def mostrar_todos_los_jugadores_y_su_posicion (self) -> None:
        """
        Recorre la lista de jugadores, mediante metodos de la clase jugador obtiene el nombre y la posición de cada jugador. 
        Luego la imprime.
        Recibe: self.
        Devuelve: nada.
        """
        for jugador in self.lista_de_jugadores:
            nombre = jugador.obtener_nombre_jugador
            posicion = jugador.obtener_posicion_jugador
            print(f"{nombre} - {posicion}")
    
    #2
    def seleccionar_jugador_y_mostrar_sus_estadisticas (self) -> None:
        """
        Pregunta por un numero y valida que lo sea. Valida que ese numero coincida con el indice de algun jugador de la lista.
        Si es asi imprime sus estadisticas. Luego pregunta si quiere importarlas a un archivo CSV.
        Recibe: self.
        Devuelve: nada.
        """
        cantidad_de_jugadores = len(self.lista_de_jugadores)
        jugador_seleccionado = input(f"Seleccione un jugador por su índice (1 - {cantidad_de_jugadores}): ")
        
        while re.match("[1-9]+", jugador_seleccionado) == None:
            jugador_seleccionado = input(f"No existe ese jugador_seleccionado. Seleccione un jugador por su índice (1 - {cantidad_de_jugadores}): ")
        if re.match("[1-9]+", jugador_seleccionado):
            jugador_seleccionado = int(jugador_seleccionado) - 1
            try:
                if jugador_seleccionado <= cantidad_de_jugadores:
                    estadisticas_jugador = self.lista_de_jugadores[jugador_seleccionado].obtener_estadisticas_completas()
                    print(self.lista_de_jugadores[jugador_seleccionado].obtener_nombre_jugador)
                    for clave, valor in estadisticas_jugador.items():
                        print(f"{clave.capitalize()} : {valor}")
                    
                    #3
                    pregunta_csv = input("¿Querés añadir estas estadisticas a un csv? (Si|No): ").lower()
                    while pregunta_csv != "si" and pregunta_csv != "no":
                        pregunta_csv = input("Tiene que responder Si o No: ").lower()
                    if pregunta_csv == "si":
                        self.crear_csv(self.lista_de_jugadores, jugador_seleccionado, True)
                        print("Información enviada exitosamente")
                    elif pregunta_csv == "no":
                        print("No se realizará la conversión a csv")
            except IndexError:
                print("Indice no encontrado")
    
    #3
    def crear_csv(self, lista, indice: int, ejercicio_3 : bool) -> None:
        """
        Consigue todos los datos que va a importar al CSV, dependiendo del ejercicio que quiera. 
        Si el archivo CSV existe, lo lee linea por linea.
        En caso de que la linea que se quiere importar ya exista, no se importa, si no existe, la crea.
        Si el archivo CSV no existe, lo crea, crea una primera linea con los nombres de los datos que luego agregara.
        Recibe: self, un dato int y un dato bool.
        Devuelve: nada.
        """
        
        lista_datos = []
        ruta = ""
        if ejercicio_3:
            ruta = ruta_de_csv
            nombre = lista[indice].obtener_nombre_jugador
            lista_datos.append(nombre)
            posicion = lista[indice].obtener_posicion_jugador
            lista_datos.append(posicion)
            estadisticas = lista[indice].obtener_estadisticas_completas()
            for v in estadisticas.values():
                lista_datos.append(v)
        
        else:
            ruta = r"Parcial\Sokolowski.csv"
            nombre = lista[indice].obtener_nombre_jugador
            lista_datos.append(nombre)
            temporadas = lista[indice].obtener_estadisticas_completas()['temporadas']
            lista_datos.append(temporadas)
            

        try:
            nueva_linea_csv = ','.join(map(str, lista_datos))
            with open(ruta, 'r+') as archivo:
                lineas = archivo.readlines()

                if nueva_linea_csv + "\n" in lineas:
                    print("La línea ya existe en el archivo CSV. No se ha añadido.")
                else:
                    archivo.write(nueva_linea_csv + "\n")
        except FileNotFoundError:
            with open(ruta, 'w', encoding= "utf-8") as file:
                if ejercicio_3:
                    claves =[
                        "Nombre",
                        "Posicion",
                        "Temporadas",
                        "Puntos totales",
                        "Promedio puntos por partido",
                        "Rebotes totales",
                        "Promedio rebotes por partido",
                        "Asistencias totales",
                        "Promedio asistencias por partido",
                        "Robos totales",
                        "Bloqueos totales",
                        "Porcentaje tiros de campo",
                        "Porcentaje tiros libres",
                        "Porcentaje tiros triples"]
                else:
                    claves =[
                        "Nombre",
                        "Temporadas"
                    ]
                titulos = ','.join(map(str, claves))
                file.write(titulos)
                file.write("\n")
                nueva_linea_csv = ','.join(map(str, lista_datos))
            
                file.write(nueva_linea_csv + "\n")
    #4
    def preguntar_si_quiere_volver_a_ingresar_dato (self, booleano : bool) -> bool:
        """
        Si el booleano vale True, pregunta si desea volver a escribir el nombre del jugador.
        Si la respuesta es si, no cambia el valor del booleano para que el programa se ejecute devuelta.
        Si la respuesta es no, cambia el valor del booleano para que el programa termine.
        Recibe: self y un dato bool.
        Devuelve: un dato bool.
        """
        if booleano:
            respuesta = input("El nombre de jugador no existe o está mal escrito. ¿Desea volver a escribirlo? (Si|No): ").lower()
            while respuesta != "si" and respuesta != "no":
                respuesta = input("Tiene que responder Si o No: ").lower()
            if respuesta == "no":
                booleano = False
        
        return booleano
        
    def seleccionar_jugador_y_mostrar_sus_logros (self) -> None:
        """
        Pide el nombre de un jugador y lo valida. 
        Si el nombre ingresado corresponde con el nombre de alguno de los jugadores de la lista, muestra sus logros.
        Recibe: self.
        Devuelve: nada.
        """
        patron = "[a-zA-Z ]+$"
        bandera = True
        while bandera:

            jugador_seleccionado = input("Ingrese el nombre del jugador que desea elegir: ")
            while re.match(patron, jugador_seleccionado, re.IGNORECASE) == None:
                jugador_seleccionado = input("El nombre debe estar compuesto por letras. Ingreselo devuelta: ")

            for jugador in self.lista_de_jugadores:
                if re.match(jugador_seleccionado, jugador.obtener_nombre_jugador, re.IGNORECASE):
                    bandera = False
                    print(f"Logros de {jugador.obtener_nombre_jugador}:")
                    for logro in jugador.obtener_logros_jugador:
                        print(logro)

            bandera = self.preguntar_si_quiere_volver_a_ingresar_dato(bandera)
    
    #5
    def promedio_de_puntos_por_partido_del_equipo (self) -> None:
        """
        Para cada jugador de la lista obtiene su promedio de puntos por partido para realizar un promedio todos.
        Ordena la lista de menor a mayor mediante un quicksort. 
        Luego recorre la lista ordenada mostrando el nombre y el promedio de puntos por partidos de cada jugador.
        Recibe: self.
        Devuelve: nada.
        """
        cantidad_de_jugadores = len(self.lista_de_jugadores)
        suma_de_promedios_de_jugadores = 0
        for jugador in self.lista_de_jugadores:
            estadisticas = jugador.obtener_estadisticas_jugador
            suma_de_promedios_de_jugadores += estadisticas.obtener_promedio_puntos_x_partido
        
        try:
            promedio_puntos_por_partido_equipo = suma_de_promedios_de_jugadores / cantidad_de_jugadores
        except ZeroDivisionError:
            print("No se puede encontrar el promedio de puntos del equipo si no existen jugadores dentro de el")
        else:
            promedio_puntos_por_partido_equipo = str(promedio_puntos_por_partido_equipo) 
            print(f"El promedio de promedios de puntos por partido de todo el equipo es de: {promedio_puntos_por_partido_equipo[:4]}")
            lista_promedios_ordenada = self.quick_sort(self.lista_de_jugadores, True, "promedio_puntos_por_partido")
             
            for jugador in lista_promedios_ordenada:
                print(f"{jugador.obtener_nombre_jugador} - {jugador.obtener_estadisticas_completas()['promedio_puntos_por_partido']}")
        
        
    def quick_sort (self, lista : list[Jugador], ascendente : bool, clave) -> function:
        """
        Ordena los datos de menor a mayor o de mayor a menor dependiendo si ascendente es True o False.
        Recibe: self, una lista de objetos Jugador, un booleano y una clave.
        Devuelve: devuelve la función aplicada a listas cada vez más chicas hasta que este ordenada.
        """
        if len(lista) < 2:
            return lista
        else:
            lista_de_jugadores_a_ordenar = lista.copy()
            if ascendente:
                pivot = lista_de_jugadores_a_ordenar.pop()
            else:
                pivot = lista_de_jugadores_a_ordenar.pop(0)
            numeros_mas_grandes = []
            numeros_mas_chicos = []
            
            for jugador in lista_de_jugadores_a_ordenar:
                if jugador.estadisticas_completas.get(clave) > pivot.estadisticas_completas.get(clave):
                    numeros_mas_grandes.append(jugador)
                elif jugador.estadisticas_completas.get(clave) <= pivot.estadisticas_completas.get(clave):
                    numeros_mas_chicos.append(jugador)
        if ascendente:    
            return self.quick_sort(numeros_mas_chicos, ascendente, clave) + [pivot] + self.quick_sort(numeros_mas_grandes, ascendente, clave)
        else:
            return self.quick_sort(numeros_mas_grandes, ascendente, clave) + [pivot] + self.quick_sort(numeros_mas_chicos, ascendente, clave)                                                           
                
    #6
    def seleccionar_jugador_y_mostrar_si_pertence_al_sdlf (self) -> None:
        """
        Pide el nombre de un jugador y lo valida. 
        Si el nombre ingresado corresponde con el nombre de alguno de los jugadores de la lista, valida si es miembro o no del Salon de la Fama.
        Recibe: self.
        Devuelve: nada.
        """
        patron = "[a-zA-Z ]+$"
        bandera = True
        while bandera:
            jugador_seleccionado = input("Ingrese el nombre del jugador que desea elegir: ")
            while re.match(patron, jugador_seleccionado, re.IGNORECASE) == None:
                jugador_seleccionado = input("El nombre debe estar compuesto por letras. Ingreselo devuelta: ")

            for jugador in self.lista_de_jugadores:
                if re.match(jugador_seleccionado, jugador.obtener_nombre_jugador, re.IGNORECASE):
                    bandera = False
                    if "Miembro del Salon de la Fama del Baloncesto" in jugador.obtener_logros_jugador:
                        print(f"{jugador.obtener_nombre_jugador} es miembro del Salón de la Fama del Baloncesto.")
                    else:
                        print(f"{jugador.obtener_nombre_jugador} no es miembro del Salón de la Fama del Baloncesto.")
        
        bandera = self.preguntar_si_quiere_volver_a_ingresar_dato(bandera)
                    
    #7
    def calcular_y_mostrar_jugador_con_mas_rebotes (self) -> None:
        """
        Calcula el mayor numero de rebotes y el jugador que lo posee. Luego lo imprime
        Recibe: self.
        Devuelve: nada.
        """
        mayor_numero_rebotes = None
        for jugador in self.lista_de_jugadores:
            if mayor_numero_rebotes == None or mayor_numero_rebotes < jugador.obtener_estadisticas_jugador.obtener_rebotes_totales:
                jugador_con_mas_rebotes = jugador.obtener_nombre_jugador
                mayor_numero_rebotes = jugador.obtener_estadisticas_jugador.obtener_rebotes_totales
        
        print (f"El jugador con más rebotes totales del dream team es: {jugador_con_mas_rebotes} con {mayor_numero_rebotes}")
    
    #8
    #A
    def listar_jugadores_ordenados_por_la_cantidad_de_temporadas (self) -> None:
        """
        Ordena la lista de mayor a menor mediante un quicksort. 
        Luego recorre la lista ordenada mostrando el nombre y las temporadas jugadas de cada jugador.
        Despues da la opción de crear un archivo CSV y/o un archivo JSON.
        Recibe: self.
        Devuelve: nada.
        """
        try:
            lista_temporadas_ordenada = self.quick_sort(self.lista_de_jugadores, False, "temporadas")
        except:
            print("Error con el archivo") 
        else:   
            for jugador in lista_temporadas_ordenada:
                print(f"{jugador.obtener_nombre_jugador} - {jugador.obtener_estadisticas_completas()['temporadas']}")
                indice_de_jugador = lista_temporadas_ordenada.index(jugador)
            
        #B
            pregunta_csv = input("¿Querés añadir estas estadisticas a un csv? (Si|No): ").lower()
            while pregunta_csv != "si" and pregunta_csv != "no":
                pregunta_csv = input("Tiene que responder Si o No: ").lower()
            if pregunta_csv == "si":
                for jugador in lista_temporadas_ordenada:
                    indice_de_jugador = lista_temporadas_ordenada.index(jugador)
                    self.crear_csv(lista_temporadas_ordenada, indice_de_jugador, False)
                print("Información enviada exitosamente")
            elif pregunta_csv == "no":
                print("No se realizará la conversión a csv")
        
        #C
            pregunta_json = input("¿Querés añadir estas estadisticas a un json? (Si|No): ").lower()
            while pregunta_json != "si" and pregunta_json != "no":
                pregunta_json = input("Tiene que responder Si o No: ").lower()
            if pregunta_json == "si":
                lista_diccionarios_jugador_temporadas = []
                for jugador in lista_temporadas_ordenada:
                    diccionario_jugador_temporadas = {}
                    diccionario_jugador_temporadas.update({"Nombre" : jugador.obtener_nombre_jugador})
                    diccionario_jugador_temporadas.update({"Temporadas Jugadas" : jugador.obtener_estadisticas_completas()['temporadas']})
                    lista_diccionarios_jugador_temporadas.append(diccionario_jugador_temporadas)
                self.crear_json(lista_diccionarios_jugador_temporadas)    
            elif pregunta_json == "no":
                print("No se realizará la conversión a json")
        
    def crear_json (self, lista_de_diccionarios : list[dict]) -> None:
        """
        Pregunta un nombre y lo valida para darselo a un archivo Json que creará posteriormente.
        Recibe: self y una lista de diccionarios.
        Devuelve: nada.
        """
        nombre_de_archivo = input("Ingrese el nombre que desea que tenga el archivo: ")
        while re.match("[a-zA-Z0-9_ ]+$", nombre_de_archivo) == None:
            print("Caracteres invalidos en el nombre. Caracteres válidos: minúsculas, mayusculas, números y guiones bajos.")
            nombre_de_archivo = input("Vuelva a ingresar el nombre que desea que tenga el archivo: ")
        ruta = f"Parcial\{nombre_de_archivo}.json"
        try:
            with open(ruta, "w", encoding = "utf-8") as archivo_json:
                contenido = {"Lista de jugadores" : lista_de_diccionarios}
                json.dump(contenido, archivo_json, indent = 4)
                print("Archivo creado")
        except:
            print("Error con el archivo")
        
            
        
    
    
                    

              
        
        
    
            
        
if __name__ == "__main__":             
    dream_team = Equipo(ruta_de_archivo)
    # dream_team.mostrar_todos_los_jugadores_y_su_posicion() #1
    #dream_team.seleccionar_jugador_y_mostrar_sus_estadisticas() #2 y 3
    #dream_team.seleccionar_jugador_y_mostrar_sus_logros()#4
    #dream_team.promedio_de_puntos_por_partido_del_equipo()#5
    #dream_team.seleccionar_jugador_y_mostrar_si_pertence_al_sdlf()#6
    #dream_team.calcular_y_mostrar_jugador_con_mas_rebotes()#7
    #dream_team.listar_jugadores_ordenados_por_la_cantidad_de_temporadas()#8 A y B
    


