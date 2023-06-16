import os
import random
import math
import matplotlib.pyplot as plt

option = 1

while option:
    #Menu
    ############################################################################
    print("Elija una de las siguientes opciones:")
    print("1) Modo Manual")
    print("2) Modo Aleatorio")
    print("3) Salir")

    option = int(input())

    if option in (1, 2, 3):
        if option == 1:
            print("Indique el valor de n en un intervalo de [2, 10^7]: ")
            size = int(input())
            
            if size > 10e7 or size < 2:
                os.system("clear")
                print("Valor de n fuera de rango, intente de nuevo!\n")
                continue
        elif option == 2:
            size = random.randint(2, 10**7)
            print("El valor generado para n es {}".format(size))
        else:
            print("\nSesion terminada")
            break
    else:
        print("Opcion Invalida")
        continue

    print("Espere un momento...")
    ############################################################################

    # Genera Lenguaje
    ############################################################################
    binary_file = open("binary_output.txt", "w")
    decimal_file = open("decimal_output.txt", "w")

    binary_file.write("L = {e")
    decimal_file.write("L = {e")

    # Algoritmo de Eratóstenes para obtener números primos
    numbers = list(range(2, size + 1))

    for p in numbers:
        if p is not None:
            binary_file.write(", " + str(bin(p))[2:])
            decimal_file.write(", " + str(p))
            for multiple in range(p * 2, size + 1, p):
                numbers[multiple - 2] = None

    binary_file.write("}"), decimal_file.write("}")
    binary_file.close(), decimal_file.close()
    ############################################################################

    with open("binary_output.txt", "r") as file:
        result = file.read()
        
        ones_count = 0
        y = []

        for char in result:
            if char == "," or char == "}":
                y.append(ones_count)
                # ones_count = 0
            elif char == "1":
                ones_count += 1

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

    os.system("clear")
