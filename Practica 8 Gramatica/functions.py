import random

def validateStr(str):
    for c in str:
        if not c in ("(", ")"):
            return 1

    return 0

def createStr(size):
    string = ""

    for i in range(size):
        string += random.choice(["(", ")"])

    return string

def CFG(str):
    output = open("output.txt", "w")
    steps = "B"
    str += " "

    output.write("Cadena: " + str + "\n\n")
    output.write("0, " + steps + "\n")

    for i, c in enumerate(str):
        if c == "(":
            if steps[i] == "B":
                steps = steps[0:i] + "(RB" + steps[i + 1:]
            elif steps[i] == "R":
                steps = steps[0:i] + "(RR" + steps[i + 1:]
        elif c == ")":
            if steps[i] == "B":
                break
            elif steps[i] == "R":
                steps = steps[0:i] + ")" + steps[i + 1:]
        elif c == " ":
            if steps[i] == "B":
                steps = steps[0:i] + "" + steps[i + 1:]

        output.write("{}, ".format(i + 1) + steps + "\n")

    output.close()

    if ("R" in steps) or ("B" in steps):
        return 0
    else:
        return 1