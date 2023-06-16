# IPN - Escuela Superior de Computación
# Autor: Jimenez Luna Rodrigo Efren
# Grupo: 4CM2

import random
import os
import time
import graphviz
from tqdm import tqdm

# Automata que comprueba si la cadena cumple con la paridad
###############################
def parity_DFA():
    string = ""
    state = "q0"

    for i in range(8):
        c = str(random.getrandbits(1))
        string += c

        if state == "q0":
            if c == "1":
                state = "q1"
            else:
                state = "q3"
        elif state == "q1":
            if c == "1":
                state = "q0"
            else:
                state = "q2"
        elif state == "q2":
            if c == "1":
                state = "q3"
            else:
                state = "q1"
        elif state == "q3":
            if c == "1":
                state = "q2"
            else:
                state = "q0"

    if state == "q0":
        return True, string
    else:
        return False, string
###############################

# Inicia el procotolo ya sea encendido o apagado de forma aleatoria
def start_protocol():
    state = random.getrandbits(1)
    executions = 0

    if state == 0:
        os.system("clear")
        print("El protocolo se encuentra apagado.\n".format(executions))
        return

    while state:
        state = random.getrandbits(1)

        os.system("clear")
        print("Generando cadenas\n")
        time.sleep(1)
        os.system("clear")
        print("Generando cadenas.\n")
        time.sleep(1)
        os.system("clear")
        print("Generando cadenas..\n")
        time.sleep(1)
        os.system("clear")
        print("Generando cadenas...\n")

        print("Iniciando analisis de cadenas:\n")

        strings_file = open("strings.txt", "a+")
        accepted_file = open("approved_strings.txt", "a+")
        rejected_file = open("rejected_strings.txt", "a+")

        # Ejecuta el AFD de paridad para las 10^6 cadenas binarias
        for i in tqdm(range(10)):
            result, string = parity_DFA()

            strings_file.write(string + "\n")

            if result:
                accepted_file.write(string + "\n")
            else:
                rejected_file.write(string + "\n")
        
        accepted_file.close()
        rejected_file.close()
        strings_file.close()

        executions += 1

    os.system("clear")
    print("El protocolo se ejecuto {} veces, ahora se encuentra apagado.\n".format(executions))

def show_automata():
    os.system("clear")

    DFA_graph = graphviz.Digraph('AFD de Paridad')
    DFA_graph.attr(rankdir='LR')

    # Inicia diagrama del protocolo
    DFA_graph.attr('node', shape='circle')
    DFA_graph.node('Listo')

    DFA_graph.attr('node', shape='plaintext')
    DFA_graph.edge('', 'Listo', label='Inicio')

    DFA_graph.attr('node', shape='circle')
    DFA_graph.edge('Listo', 'Enviar', label='Entrada de cadena')
    DFA_graph.edge('Enviar', 'Enviar', label='Espera 3 segundos')
    DFA_graph.edge('Enviar', 'Paridad', label='')
    DFA_graph.edge('Paridad', 'Listo', label='')

    # Inicia diagrama del AFD
    DFA_graph.attr('node', shape='doublecircle')
    DFA_graph.node('Q0')
    DFA_graph.node('Paridad')

    DFA_graph.attr('node', shape='plaintext')
    DFA_graph.edge('', 'Q0', label='Paridad')

    DFA_graph.attr('node', shape='circle')
    DFA_graph.edge('Q0', 'Q1', label='1')
    DFA_graph.edge('Q0', 'Q3', label='0')
    DFA_graph.edge('Q1', 'Q0', label='1')
    DFA_graph.edge('Q1', 'Q2', label='0')
    DFA_graph.edge('Q2', 'Q1', label='0')
    DFA_graph.edge('Q2', 'Q3', label='1')
    DFA_graph.edge('Q3', 'Q2', label='1')
    DFA_graph.edge('Q3', 'Q0', label='0')

    DFA_graph.render('Automata', view=True)
