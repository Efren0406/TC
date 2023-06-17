import random
import time

def generatePal(size):
    output = open("output.txt", "w")
    str = "P"
    current_size = 0

    output.write("Tamaño de la cadena a generar: {}\n\n".format(size))
    output.write("-> P\n")

    random.seed(time.time())

    for i in range(size + 1):
        if current_size <= size - 2:
            if random.choice([True, False]):
                str = str.replace("P", "0P0")
                output.write("-> " + str + "\n")
                current_size += 2
            else:
                str = str.replace("P", "1P1")
                output.write("-> " + str + "\n")
                current_size += 2
        elif current_size == size - 1:
            if random.choice([True, False]):
                str = str.replace("P", "0")
                output.write("-> " + str + "\n")
            else:
                str = str.replace("P", "1")
                output.write("-> " + str + "\n")
            break
        else:
            str = str.replace("P", "")
            output.write("-> " + str + "\n")
            break

    output.close()

    return str