# IPN - Escuela Superior de Computación
# Autor: Jimenez Luna Rodrigo Efren
# Grupo: 4CM2

from functions import *
import os

if __name__ == "__main__": 
    while True:
        option = 0

        #Menu
        ############################
        print("Elija una de las siguientes tres opciones del menu:")
        print("1) Iniciar protocolo")
        print("2) Graficar Automata")
        print("3) Salir")

        option = int(input())

        if option == 1:
            start_protocol()
        elif option == 2:
            show_automata()
        elif option == 3:
            break
        elif option != 0:
            os.system("clear")
            print("La opción no es valida, vuelva a intentarlo!\n")
        ############################
