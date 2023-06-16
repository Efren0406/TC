#   IPN - Escuela Superior de Computación   
#   Autor: Jimenez Luna Rodrigo Efren
#   Grupo: 4CM2

import itertools
import os
import random
import matplotlib.pyplot as plt
import math

from tqdm import tqdm

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
            print("Indique el valor de n en un intervalo de [0, 1000]: ")
            size = int(input())
            if size > 1000 or size < 0:
                print("Valor de n fuera de reango, intente de nuevo!\n")
                continue
        elif option == 2:
            size = random.randint(0, 1001)
            print("El valor generado para n es {}".format(size))
        else:
            print("Sesion terminada")
            break;
    else:
        print("Opcion Invalida")
        continue;	
    ############################################################################

    #Genera Universo
    ############################################################################
    file = open("output.txt", "w")
    file.write("L = {e")
    y = [0]

    # Solo se calculan las combinaciones para un valor de n diferente de 0
    if size > 0:
        ones_count = 0
        aux = ['0', '1']

        file.write(", 0, 1")

        y.append(1)

        with tqdm(total = 2**(size + 1) - 4) as pgbar:
            for i in range(size-1):
                memory = aux
                aux = []
                # Concatenación del resultado anterior con el par ordenado {0, 1}
                for j in ['0', '1']: 
                    for k in memory:
                        file.write(", " + j + k)
                        aux.append(j + k)
                        ones_count += (j + k).count('1')
                        pgbar.update(1)

                y.append(ones_count)
                ones_count = 0
    
    file.write("}")
    file.close()
    ############################################################################

    #Graficación
    ############################################################################
    plt.plot(y)
    plt.xlabel('String')
    plt.ylabel('Number of 1s')
    plt.title('String and 1s relation')
    plt.show()

    log10_values = []

    for value in y:
        if value != 0:
            log10_values.append(math.log10(value))

    plt.plot(log10_values)
    plt.xlabel('String')
    plt.ylabel('Log10 of 1s')
    plt.title('Log10 ones and string relation')
    plt.show()
    ############################################################################
