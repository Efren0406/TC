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
            print("Ingrese una cadena de ('s y )'s menor de 1,000 caracteres: ")
            str = input()
            # print("{}".format(str))

            if validateStr(str):
                print("La cadena contiene caracteres diferentes de ( y )!\n")
                continue

            if len(str) > 1000:
                print("La cadena contiene más caracteres de los permitidos\n")
                continue
        elif option == 2:
            str = createStr(random.randint(1, 100000))
            print("Evaluando la cadena de tamaño {} en el automata...".format(len(str)))
        else:
            print("Sesion terminada")
            break;
    else:
        print("Opcion Invalida")
        continue;	

    if CFG(str):
        print("La cadena es válida!\n")
        print("Presione <Enter> para continuar\n")
        input()
        os.system("clear")
    else:
        print("La cadena no se encuentra en la gramática!\n")
        print("Presione <Enter> para continuar\n")
        input()
        os.system("clear")