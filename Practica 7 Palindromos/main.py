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
            print("Ingrese el tamaño de la cadena en un intervalo [1, 100000]: ")
            size = int(input())
            # print("{}".format(str))

            if size > 100000 or size < 0:
                print("El intervalo es inválido\n")
                continue
        elif option == 2:
            size = random.randint(1, 100000)
            print("Generando la cadena de tamaño {}...".format(size))
        else:
            print("Sesion terminada")
            break
    else:
        print("Opcion Invalida")
        continue;	

    str = generatePal(size)

    if size < 20:
        print("La cadena resultante es: " + str + "\n")
    else:
        print("La cadena se muestra en el archivo output.txt\n")