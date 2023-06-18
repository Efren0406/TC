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

def TM(str):
    str += "  "
    output = open("output.txt", "w")
    state = "Q0"
    symbol = ""
    pointer = 0

    output.write("Cadena: " + str + "\n\n")

    while True:
        if state == "Q0":
            if str[pointer] == "0":
                state = "Q1"
                symbol = "X"
                str = str[0:pointer] + symbol + str[pointer + 1:]
                pointer += 1
                output.write("(" + state + ", " + symbol + ", R) ├\n")
            elif str[pointer] == "1":
                output.write("\nLa cadena no se encuentra en el lenguaje {0^n 1^n | n >= 1}!\n")
                output.close()
                return 0
            elif str[pointer] == "X":
                output.write("\nLa cadena no se encuentra en el lenguaje {0^n 1^n | n >= 1}!\n")
                output.close()
                return 0
            elif str[pointer] == "Y":
                state = "Q3"
                symbol = "Y"
                str = str[0:pointer] + symbol + str[pointer + 1:]
                pointer += 1
                output.write("(" + state + ", " + symbol + ", R) ├\n")
            elif str[pointer] == " ":
                output.write("\nLa cadena no se encuentra en el lenguaje {0^n 1^n | n >= 1}!\n")
                output.close()
                return 0
        if state == "Q1":
            if str[pointer] == "0":
                state = "Q1"
                symbol = "0"
                str = str[0:pointer] + symbol + str[pointer + 1:]
                pointer += 1
                output.write("(" + state + ", " + symbol + ", R) ├\n")
            elif str[pointer] == "1":
                state = "Q2"
                symbol = "Y"
                str = str[0:pointer] + symbol + str[pointer + 1:]
                pointer -= 1
                output.write("(" + state + ", " + symbol + ", L) ├\n")
            elif str[pointer] == "X":
                output.write("\nLa cadena no se encuentra en el lenguaje {0^n 1^n | n >= 1}!\n")
                output.close()
                return 0
            elif str[pointer] == "Y":
                state = "Q1"
                symbol = "Y"
                str = str[0:pointer] + symbol + str[pointer + 1:]
                pointer += 1
                output.write("(" + state + ", " + symbol + ", R) ├\n")
            elif str[pointer] == " ":
                output.write("\nLa cadena no se encuentra en el lenguaje {0^n 1^n | n >= 1}!\n")
                output.close()
                return 0
        if state == "Q2":
            if str[pointer] == "0":
                state = "Q2"
                symbol = "0"
                str = str[0:pointer] + symbol + str[pointer + 1:]
                pointer -= 1
                output.write("(" + state + ", " + symbol + ", L) ├\n")
            elif str[pointer] == "1":
                output.write("\nLa cadena no se encuentra en el lenguaje {0^n 1^n | n >= 1}!\n")
                output.close()
                return 0
            elif str[pointer] == "X":
                state = "Q0"
                symbol = "X"
                str = str[0:pointer] + symbol + str[pointer + 1:]
                pointer += 1
                output.write("(" + state + ", " + symbol + ", R) ├\n")
            elif str[pointer] == "Y":
                state = "Q2"
                symbol = "Y"
                str = str[0:pointer] + symbol + str[pointer + 1:]
                pointer -= 1
                output.write("(" + state + ", " + symbol + ", L) ├\n")
            elif str[pointer] == " ":
                output.write("\nLa cadena no se encuentra en el lenguaje {0^n 1^n | n >= 1}!\n")
                output.close()
                return 0
        if state == "Q3":
            if str[pointer] == "0":
                output.write("\nLa cadena no se encuentra en el lenguaje {0^n 1^n | n >= 1}!\n")
                output.close()
                return 0
            elif str[pointer] == "1":
                output.write("\nLa cadena no se encuentra en el lenguaje {0^n 1^n | n >= 1}!\n")
                output.close()
                return 0
            elif str[pointer] == "X":
                output.write("\nLa cadena no se encuentra en el lenguaje {0^n 1^n | n >= 1}!\n")
                output.close()
                return 0
            elif str[pointer] == "Y":
                state = "Q3"
                symbol = "Y"
                str = str[0:pointer] + symbol + str[pointer + 1:]
                pointer += 1
                output.write("(" + state + ", " + symbol + ", R) ├\n")
            elif str[pointer] == " ":
                state = "Q4"
                symbol = "B"
                str = str[0:pointer] + symbol + str[pointer + 1:]
                pointer += 1
                output.write("(" + state + ", " + symbol + ", R) ├\n")
        if state == "Q4":
            break

    output.close()

    return 1

def animateTM(str):
    output = open("output.txt", "w")
    state = "Q0"
    symbol = ""
    pointer = 0
    start = 10
    str += "  "

    output.write("Cadena: " + str + "\n\n")

    root = tk.Tk()
    root.title("Push Down Automata Animation")
    root.geometry("600x400")
    canvas = tk.Canvas(root, width=600, height=400)
    canvas.pack()

    canvas.create_rectangle(265, 50, 335, 120, fill="lightgreen")
    canvas.create_line(300, 120, 300, 170, arrow=tk.LAST, width=2)
    canvas.create_text(300, 85, text=state, font=("Arial", 14), anchor=tk.CENTER)

    for i in range(22):
        canvas.create_rectangle(-15 + i * 30, 170, 15 + i * 30, 200, fill="lightgreen")
        if i >= start - pointer and i < start + len(str) - 2 - pointer:
            canvas.create_text(i * 30, 185, text=str[i - start + pointer], font=("Arial", 14), anchor=tk.CENTER)
        else:
            canvas.create_text(i * 30, 185, text="B", font=("Arial", 14), anchor=tk.CENTER)

    while True:
        root.update()
        time.sleep(.5)
        canvas.delete(tk.ALL)

        if state == "Q0":
            if str[pointer] == "0":
                state = "Q1"
                symbol = "X"
                str = str[0:pointer] + symbol + str[pointer + 1:]
                pointer += 1
                output.write("(" + state + ", " + symbol + ", R) ├\n")
            elif str[pointer] == "1":
                output.write("\nLa cadena no se encuentra en el lenguaje {0^n 1^n | n >= 1}!\n")
                output.close()
                break
            elif str[pointer] == "X":
                output.write("\nLa cadena no se encuentra en el lenguaje {0^n 1^n | n >= 1}!\n")
                output.close()
                break
            elif str[pointer] == "Y":
                state = "Q3"
                symbol = "Y"
                str = str[0:pointer] + symbol + str[pointer + 1:]
                pointer += 1
                output.write("(" + state + ", " + symbol + ", R) ├\n")
            elif str[pointer] == " ":
                output.write("\nLa cadena no se encuentra en el lenguaje {0^n 1^n | n >= 1}!\n")
                output.close()
                break
        elif state == "Q1":
            if str[pointer] == "0":
                state = "Q1"
                symbol = "0"
                str = str[0:pointer] + symbol + str[pointer + 1:]
                pointer += 1
                output.write("(" + state + ", " + symbol + ", R) ├\n")
            elif str[pointer] == "1":
                state = "Q2"
                symbol = "Y"
                str = str[0:pointer] + symbol + str[pointer + 1:]
                pointer -= 1
                output.write("(" + state + ", " + symbol + ", L) ├\n")
            elif str[pointer] == "X":
                output.write("\nLa cadena no se encuentra en el lenguaje {0^n 1^n | n >= 1}!\n")
                output.close()
                break
            elif str[pointer] == "Y":
                state = "Q1"
                symbol = "Y"
                str = str[0:pointer] + symbol + str[pointer + 1:]
                pointer += 1
                output.write("(" + state + ", " + symbol + ", R) ├\n")
            elif str[pointer] == " ":
                output.write("\nLa cadena no se encuentra en el lenguaje {0^n 1^n | n >= 1}!\n")
                output.close()
                break
        elif state == "Q2":
            if str[pointer] == "0":
                state = "Q2"
                symbol = "0"
                str = str[0:pointer] + symbol + str[pointer + 1:]
                pointer -= 1
                output.write("(" + state + ", " + symbol + ", L) ├\n")
            elif str[pointer] == "1":
                output.write("\nLa cadena no se encuentra en el lenguaje {0^n 1^n | n >= 1}!\n")
                output.close()
                break
            elif str[pointer] == "X":
                state = "Q0"
                symbol = "X"
                str = str[0:pointer] + symbol + str[pointer + 1:]
                pointer += 1
                output.write("(" + state + ", " + symbol + ", R) ├\n")
            elif str[pointer] == "Y":
                state = "Q2"
                symbol = "Y"
                str = str[0:pointer] + symbol + str[pointer + 1:]
                pointer -= 1
                output.write("(" + state + ", " + symbol + ", L) ├\n")
            elif str[pointer] == " ":
                output.write("\nLa cadena no se encuentra en el lenguaje {0^n 1^n | n >= 1}!\n")
                output.close()
                break
        elif state == "Q3":
            if str[pointer] == "0":
                output.write("\nLa cadena no se encuentra en el lenguaje {0^n 1^n | n >= 1}!\n")
                output.close()
                break
            elif str[pointer] == "1":
                output.write("\nLa cadena no se encuentra en el lenguaje {0^n 1^n | n >= 1}!\n")
                output.close()
                break
            elif str[pointer] == "X":
                output.write("\nLa cadena no se encuentra en el lenguaje {0^n 1^n | n >= 1}!\n")
                output.close()
                break
            elif str[pointer] == "Y":
                state = "Q3"
                symbol = "Y"
                str = str[0:pointer] + symbol + str[pointer + 1:]
                pointer += 1
                output.write("(" + state + ", " + symbol + ", R) ├\n")
            elif str[pointer] == " ":
                state = "Q4"
                symbol = "B"
                str = str[0:pointer] + symbol + str[pointer + 1:]
                pointer += 1
                output.write("(" + state + ", " + symbol + ", R) ├\n")
        elif state == "Q4":
            break

        canvas.create_rectangle(265, 50, 335, 120, fill="lightgreen")
        canvas.create_line(300, 120, 300, 170, arrow=tk.LAST, width=2)
        canvas.create_text(300, 85, text=state, font=("Arial", 14), anchor=tk.CENTER)

        for i in range(22):
            canvas.create_rectangle(-15 + i * 30, 170, 15 + i * 30, 200, fill="lightgreen")
            if i >= start - pointer and i < start + len(str) - 2 - pointer:
                canvas.create_text(i * 30, 185, text=str[i - start + pointer], font=("Arial", 14), anchor=tk.CENTER)
            else:
                canvas.create_text(i * 30, 185, text="B", font=("Arial", 14), anchor=tk.CENTER)

    canvas.create_rectangle(265, 50, 335, 120, fill="lightgreen")
    canvas.create_line(300, 120, 300, 170, arrow=tk.LAST, width=2)
    canvas.create_text(300, 85, text=state, font=("Arial", 14), anchor=tk.CENTER)

    for i in range(22):
        canvas.create_rectangle(-15 + i * 30, 170, 15 + i * 30, 200, fill="lightgreen")
        if i >= start - pointer and i < start + len(str) - 2 - pointer:
            canvas.create_text(i * 30, 185, text=str[i - start + pointer], font=("Arial", 14), anchor=tk.CENTER)
        else:
            canvas.create_text(i * 30, 185, text="B", font=("Arial", 14), anchor=tk.CENTER)

    if state == "Q4":
        canvas.create_text(300, 250, text="Cadena válida!", font=("Arial", 14), anchor=tk.CENTER)
    else:
        canvas.create_text(300, 250, text="La cadena no pertenece al lenguaje!", font=("Arial", 14), anchor=tk.CENTER)

    root.mainloop()
    output.close()

    if state == "Q4":
        return 1
    else:
        return 0