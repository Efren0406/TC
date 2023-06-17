import random
import tkinter as tk
import time

def validateStr(str):
    for c in str:
        if not c in ("1", "0"):
            return 1

    return 0

def createStr(size):
    aproved = random.getrandbits(1)
    string = ""

    if aproved:
        for i in range(size // 2):
            string += "0"
        for i in range(size - size // 2):
            string += "1"
    else:
        for i in range(size):
            string += str(random.getrandbits(1))

    return string

def pushDownAutomata(str):
    output = open("output.txt", "w")
    state = "Q"
    symbol = ""
    count = 0

    output.write("Cadena: " + str + "\n\n")

    if str[0] == "1":
        output.write("Stack underflow!\n")
        output.close()
        print("Stack underflow!\n")
        return 0

    for i, c in enumerate(str):
        if state ==  "Q":
            if c ==  "0" and count == 0:
                count += 1
                symbol = "X"
            elif c == "0" and count > 0:
                count += 1
                symbol = "X"
            elif c == "1" and count > 0:
                count -= 1
                symbol = "ε"
                state = "P"
        elif state == "P":
            if c == "1":
                symbol = "ε"
                count -= 1
            elif c == "0":
                count = -1
                break

        output.write("("+ state + ", " + c + ", " + symbol + ") ├\n")

    output.close()

    if count == 0:
        return 1
    else:
        return 0


def animatePDA(str):
    output = open("output.txt", "w")
    state = "Q"
    symbol = ""
    count = 0
    screen_str = str
    stack = "Z"

    output.write("Cadena: " + str + "\n\n")

    root = tk.Tk()
    root.title("Push Down Automata Animation")
    root.geometry("600x400")
    canvas = tk.Canvas(root, width=600, height=400)
    canvas.pack()

    canvas.create_rectangle(250, 150, 350, 250, fill="lightgreen")

    canvas.create_text(299, 199, text=state, font=("Arial", 14))
    canvas.create_text(298, 80, text=screen_str, font=("Arial", 14), anchor=tk.NW)
    canvas.create_text(298, 300, text=stack, font=("Arial", 14), anchor=tk.NW)

    canvas.create_line(300, 150, 300, 100, arrow=tk.LAST, width=2)
    canvas.create_line(300, 250, 300, 300, arrow=tk.LAST, width=2)

    for c in str:
        root.update()
        time.sleep(1)
        canvas.delete(tk.ALL)

        screen_str = screen_str[1:]

        if state ==  "Q":
            if c ==  "0" and count == 0:
                count += 1
                symbol = "X"
            elif c == "0" and count > 0:
                count += 1
                symbol = "X"
            elif c == "1" and count > 0:
                count -= 1
                symbol = "ε"
                state = "P"
        elif state == "P":
            if c == "1":
                symbol = "ε"
                count -= 1
            elif c == "0":
                count = -1
                break

        if str[0] == "1":
            canvas.create_text(300, 200, text="Stack Underflow!", font=("Arial", 25))
            output.write("Stack underflow!\n")
            count = -1
            break

        if state == "Q":
            stack = symbol + stack
        elif state == "P":
            stack = stack[1:]
        output.write("("+ state + ", " + c + ", " + symbol + ") ├\n")

        canvas.create_rectangle(250, 150, 350, 250, fill="lightgreen")

        canvas.create_text(299, 199, text=state, font=("Arial", 14))
        canvas.create_text(298, 80, text=screen_str, font=("Arial", 14), anchor=tk.NW)
        canvas.create_text(298, 300, text=stack, font=("Arial", 14), anchor=tk.NW)

        canvas.create_line(300, 150, 300, 100, arrow=tk.LAST, width=2)
        canvas.create_line(300, 250, 300, 300, arrow=tk.LAST, width=2)

    if count == 0:
        canvas.create_text(300, 30, text="Cadena Válida!", font=("Arial", 14))
    else:
        canvas.create_text(300, 30, text="La cadena no pertenece al lenguaje!", fill="red", font=("Arial", 14))

    root.mainloop()
    output.close()

    if count == 0:
        return 1
    else:
        return 0
