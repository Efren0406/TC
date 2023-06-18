import os
import random

from functions import *

option = 1

while option:
    # Menu
    ############################################################################
    print("Elija una de las siguientes opciones:")
    print("1) Modo Manual")
    print("2) Modo Aleatorio")
    print("3) Salir")
	
    option = int(input())

    os.system("clear")

    if option in (1, 2, 3):
        if option == 1:
            print("Ingrese una cadena de 0's y 1's menor de 1,000 caracteres: ")
            str = input()
            # print("{}".format(str))

            if validateStr(str):
                print("La cadena contiene caracteres diferentes de 0 y 1!\n")

            if len(str) > 1000:
                print("La cadena contiene más caracteres de los permitidos\n")
                continue
        elif option == 2:
            str = createStr(random.randint(1, 1000))
            print("Evaluando la cadena de tamaño {} en maquina de turing...".format(len(str)))
        else:
            print("Sesion terminada")
            break
    else:
        print("Opcion Invalida")
        continue;	

    if len(str) <= 10:
        if animateTM(str):
            print("Presione <Enter> para continuar\n")
            input()
            os.system("clear")
        else:
            print("Presione <Enter> para continuar\n")
            input()
            os.system("clear")
    else:
        if TM(str):
            print("\nLa cadena es válida!\n")
            print("Presione <Enter> para continuar\n")
            input()
            os.system("clear")
        else:
            print("\nLa cadena no se encuentra en el lenguaje {0^n 1^n | n >= 1}!\n")
            print("Presione <Enter> para continuar\n")
            input()
            os.system("clear")