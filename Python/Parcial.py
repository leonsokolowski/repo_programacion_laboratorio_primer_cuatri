# Copyright (C) 2023 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

NOMBRE = "" # León Sokolowski

"""
#Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar 
    en la bolsa de valores.:

A) Para ello deberás programar el botón  para poder cargar 10 operaciones de compra 
    con los siguientes datos:
    * Nombre
    * Monto en pesos de la operación (no menor a $10000)
    * Tipo de instrumento(CEDEAR, BONOS, MEP) 
    * Cantidad de instrumentos  (no menos de cero) 
    Son 10 datos

B) Al presionar el botón mostrar 
    
    Informe 1 - Se deberán listar todos los datos de los usuarios y su posición en la lista (por terminal) 

# IMPORTANTE:
Del punto C solo deberá realizar SOLAMENTE 2 informes. 
(PRESUPONER QUE CADA CLIENTE INGRESADO ES UN CLIENTE DISTINTO, NINGUNO SE REPITE, 
no es necesario validar que no haya nombres repetidos)

Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    Informe 2 - Tome el último número de su DNI Personal (Ej 4) 
        y realice ese informe (Ej, Realizar informe 4)

    Informe 3 - Tome el último número de su DNI Personal (Ej 4), 
        y restarle al número 9 (Ej 9-4 = 5). En caso de que su DNI 
        finalice con el número 0, deberá realizar el informe 9.

    Realizar los informes correspondientes a los números obtenidos. 
        EL RESTO DE LOS INFORMES LOS DEBE IGNORAR. 
C) 
    #! 0) - Tipo de instrumento que menos se operó en total.
    #! 1) - Tipo de instrumento que más se operó en total.
    #! 2) - Cantidad de usuarios que compraron entre 50  y 200 MEP 
    #! 3) - Cantidad de usuarios que no compraron CEDEAR 
    #! 4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
    #! 5) - Nombre y posicion de la persona que menos BONOS compro
    #! 6) - Nombre y posicion del usuario que invirtio menos dinero
    #! 7) - Nombre y posicion del usuario que mas cantidad de instrumentos compró
    #! 8) - Promedio de dinero en CEDEAR  ingresado en total.  
    #! 9) - Promedio de cantidad de instrumentos  MEP vendidos en total
"""

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(f"UTN FRA - Bolsa de valores de {NOMBRE}")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text=f"Bolsa de valores {NOMBRE}", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)


        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar cartas", command=self.btn_cargar_datos_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")
        self.btn_mostrar_todos = customtkinter.CTkButton(master=self, text="Mostrar todos", command=self.btn_mostrar_todos_on_click)
        self.btn_mostrar_todos.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
        self.btn_informe_2.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3", command=self.btn_mostrar_informe_3)
        self.btn_informe_3.grid(row=6, pady=10, columnspan=2, sticky="nsew")

        self.lista_de_nombres = ["León" , "Matías" , "Marcelo" , "Cecilia" , "Cristian" , "Nacho" , "Wanda" , "Facundo" , "Miranda" , "Rocío"]
        self.lista_de_montos_de_pesos = [11000 , 13000 , 15000 , 12000 , 17000 , 19000 , 16000 , 26000 , 22000 , 20000 ]
        self.lista_de_tipos_de_instrumentos = ["cedear" , "bonos" , "mep" , "bonos" , "mep" , "cedear", "cedear" , "bonos" , "cedear" , "cedear"]
        self.lista_de_cantidades_de_instrumentos = [2 , 6 , 9 , 16 , 14 , 3 , 26 , 2 , 7, 10]
        
        #PUEDE MODIFICAR LOS DATOS A SU ANTOJO, A EFECTOS DE REALIZAR PRUEBAS
        
    def btn_mostrar_todos_on_click(self):
        pass

    def btn_mostrar_informe_1(self):
        print("Nombre: Montos en pesos: Tipo instrumento: Cantindad de instrumentos: Lugar en la lista:")
        
        for i in range (10):
            print(f"{self.lista_de_nombres[i]} {self.lista_de_montos_de_pesos[i]} {self.lista_de_tipos_de_instrumentos[i]} {self.lista_de_cantidades_de_instrumentos [i]} {i}")

    def btn_mostrar_informe_2(self):
        #! 0) - Tipo de instrumento que menos se operó en total.
        largo_de_lista = len(self.lista_de_cantidades_de_instrumentos)
        acumulador_cedear = 0
        acumulador_bonos = 0
        acumulador_mep = 0
        
        for i in range (largo_de_lista):
            
            match(self.lista_de_tipos_de_instrumentos):
                case "cedear":
                    acumulador_cedear += self.lista_de_cantidades_de_instrumentos[i]
                case "bonos": 
                    acumulador_bonos += self.lista_de_cantidades_de_instrumentos[i]
                case _:
                    acumulador_mep += self.lista_de_cantidades_de_instrumentos[i]
        
        if acumulador_cedear < acumulador_bonos and acumulador_cedear < acumulador_mep:
            instrumento_menos_operado = "cedear"
        elif acumulador_bonos < acumulador_mep:
            instrumento_menos_operado = "bonos"
        else:
            instrumento_menos_operado = "mep"
        
        print(instrumento_menos_operado)
                    
                

    def btn_mostrar_informe_3(self):
        #! 4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR 
        
        # largo_de_lista = len(self.lista_de_nombres)
        # nombre_usuario_bonos_o_cedear = None
        # cantidad_invertida_usuario_bonos_o_cedear = 0
        
        # for i in range (largo_de_lista):
        #     match(self.lista_de_tipos_de_instrumentos[i]):
        #         case "bonos":
        #             if nombre_usuario_bonos_o_cedear == None:
        #                 nombre_usuario_bonos_o_cedear = self.lista_de_nombres[i]
        #                 cantidad_invertida_usuario_bonos_o_cedear = self.lista_de_montos_de_pesos[i]
        #         case "cedear":
        #             if nombre_usuario_bonos_o_cedear == None:
        #                 nombre_usuario_bonos_o_cedear = self.lista_de_nombres[i]
        #                 cantidad_invertida_usuario_bonos_o_cedear = self.lista_de_montos_de_pesos[i]
        
        # print(nombre_usuario_bonos_o_cedear, cantidad_invertida_usuario_bonos_o_cedear)
        
        # #! 5) - Nombre y posicion de la persona que menos BONOS compro
        # largo_de_lista = len(self.lista_de_nombres)
        # cantidad_de_bonos_comprados = None
        
        # for i in range (largo_de_lista):
            
        #     if self.lista_de_tipos_de_instrumentos[i] == "bonos":
        #         if cantidad_de_bonos_comprados == None or self.lista_de_cantidades_de_instrumentos[i] < cantidad_de_bonos_comprados:
        #             cantidad_de_bonos_comprados = self.lista_de_cantidades_de_instrumentos[i]
        #             nombre_usuario_menor_cantidad_bonos = self.lista_de_nombres[i]
        #             posicion = i
            
        # print(f"El usuario que menos bonos compró fue {nombre_usuario_menor_cantidad_bonos} y esta en la posición {posicion}")
        
        #! 6) - Nombre y posicion del usuario que invirtio menos dinero
            largo_de_lista = len(self.lista_de_nombres)
            importe_pesos = 0
            
            for i in range (largo_de_lista):
                
                if importe_pesos == 0 or self.lista_de_montos_de_pesos[i] < importe_pesos:
                    importe_pesos = self.lista_de_montos_de_pesos[i]
                    nombre_menor_importe = self.lista_de_nombres[i]
                    posicion = i
            
            print(f"El usuario que menos invirtió fue {nombre_menor_importe} y esta en la posición {i}")
                
                
                
        
            

    def btn_cargar_datos_on_click(self):
        pass

if __name__ == "__main__":
    app = App()
    app.mainloop()
