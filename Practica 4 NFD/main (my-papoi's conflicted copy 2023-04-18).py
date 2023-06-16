# IPN - Escuela Superior de Computacion
# Autor: Jimenez Luna Rodrigo Efren
# Grupo: 4CM2

import os
from functions import *

while True:
    print("Elija alguna de las siguientes opciones:")
    print("1) Buscador de palabras")
    print("2) Graficar Automata")
    print("3) Salir")

    option = int(input())

    if option == 1:
        word_finder()
    elif option == 2:
        graph_automata()
    elif option == 3:
        break
    else:
        os.system("clear")
        print("Opcion invalida, por favor vuelva a intentarlo!\n")
