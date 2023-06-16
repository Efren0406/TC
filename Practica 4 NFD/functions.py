# IPN - Escuela Superior de Computacion
# Autor: Jimenez Luna Rodrigo Efren
# Grupo: 4CM2

import os
import urllib.request
from inscriptis import get_text
import graphviz

# Imprimir resultados
# La siguiente funcion toma el conteo de palabras y posiciones obtenidas
# por el AFD y las muestra en un archivo de texto
def print_results(file, words):
    for word in words:
        if 'position' in word and len(words[word]) > 0:
            file.write("La palabra ''{}'' fue encontrada {} veces en las posiciones:\n".format(word.replace('-positions', ''), words[word.replace('-positions', '')]))
            file.write(", ".join(map(str, words[word])))
            file.write("\n\n")
        elif 'position' in word:
            file.write("No se encontro la palabra {} en el texto!\n".format(word.replace('-positions', '')))
            file.write("\n")

# Buscador de Palabras con un AFD
# La funcion contiene al Automata el cual se encargara de buscar las palabras
# 'web', 'webpage', 'website', 'webmaster', 'site', 'page' e 'ebay'
def DFA_word_finder(text):
    record_file = open("record.txt", "w")
    result_file = open("result.txt", "w")
    position = 0

    words = {
        'web': 0,
        'web-positions': [],
        'webpage': 0,
        'webpage-positions': [],
        'website': 0,
        'website-positions': [],
        'webmaster': 0,
        'webmaster-positions': [],
        'page': 0,
        'page-positions': [],
        'site': 0,
        'site-positions': [],
        'ebay': 0,
        'ebay-positions': [],
    }

    state = "1"
    prev_state = "1"

    for c in text:
        position += 1

        # Automata Finito Determinista
        if state == "1":
            if c in ("w", "W"):
                state = "1251219"
            elif c in ("e", "E"):
                state = "136"
            elif c in ("s", "S"):
                state = "28"
            elif c in ("p", "P"):
                state = "32"
            else:
                state = "1"
        elif state == "1251219":
            if c in ("w", "W"):
                state = "1251219"
            elif c in ("e", "E"):
                state = "136361320"
            elif c in ("s", "S"):
                state = "28"
            elif c in ("p", "P"):
                state = "32"
            else:
                state = "1"
        elif state == "136":
            if c in ("w", "W"):
                state = "1251219"
            elif c in ("e", "E"):
                state = "136"
            elif c in ("b", "B"):
                state = "137"
            elif c in ("s", "S"):
                state = "28"
            elif c in ("p", "P"):
                state = "32"
            else:
                state = "1"
        elif state == "28":
            if c in ("i", "I"):
                state = "29"
            else:
                state = "1"
        elif state == "32":
            if c in ("a", "A"):
                state = "33"
            else:
                state = "1"
        elif state == "136361320":
            if c in ("w", "W"):
                state = "1251219"
            elif c in ("e", "E"):
                state = "136"
            elif c in ("b", "B"):
                words['web'] += 1
                words['web-positions'].append(position - 2)
                state = "137471421"
            elif c in ("s", "S"):
                state = "28"
            elif c in ("p", "P"):
                state = "32"
            else:
                state = "1"
        elif state == "29":
            if c in ("t", "T"):
                state = "30"
            else:
                state = "1"
        elif state == "33":
            if c in ("g", "G"):
                state = "34"
            else:
                state = "1"
        elif state == "137471421":
            if c in ("w", "W"):
                state = "1251219"
            elif c in ("e", "E"):
                state = "136"
            elif c in ("s", "S"):
                state = "2815"
            elif c in ("p", "P"):
                state = "328"
            elif c in ("a", "A"):
                state = "138"
            elif c in ("m", "M"):
                state = "122"
            else:
                state = "1"
        elif state == "2815":
            if c in ("i", "I"):
                state = "2916"
            else:
                state = "1"
        elif state == "328":
            if c in ("a", "A"):
                state = "339"
            else:
                state = "1"
        elif state == "137":
            if c in ("w", "W"):
                state = "1251219"
            elif c in ("e", "E"):
                state = "136"
            elif c in ("s", "S"):
                state = "28"
            elif c in ("p", "P"):
                state = "32"
            elif c in ("a", "A"):
                state = "138"
            else:
                state = "1"
        elif state == "122":
            if c in ("w", "W"):
                state = "1251219"
            elif c in ("e", "E"):
                state = "136"
            elif c in ("s", "S"):
                state = "28"
            elif c in ("p", "P"):
                state = "32"
            elif c in ("a", "A"):
                state = "123"
            else:
                state = "1"
        elif state == "2916":
            if c in ("t", "T"):
                state = "3017"
            else:
                state = "1"
        elif state == "339":
            if c in ("g", "G"):
                state = "3410"
            else:
                state = "1"
        elif state == "138":
            if c in ("w", "W"):
                state = "1251219"
            elif c in ("e", "E"):
                state = "136"
            elif c in ("s", "S"):
                state = "28"
            elif c in ("p", "P"):
                state = "32"
            elif c in ("a", "A"):
                state = "23"
            elif c in ("y", "Y"):
                words['ebay'] += 1
                words['ebay-positions'].append(position - 3)
                state = "139"
            else:
                state = "1"
        elif state == "123":
            if c in ("w", "W"):
                state = "1251219"
            elif c in ("e", "E"):
                state = "136"
            elif c in ("s", "S"):
                state = "2824"
            elif c in ("p", "P"):
                state = "32"
            else:
                state = "1"
        elif state == "139":
            if c in ("w", "W"):
                state = "1251219"
            elif c in ("e", "E"):
                state = "136"
            elif c in ("s", "S"):
                state = "28"
            elif c in ("p", "P"):
                state = "32"
            else:
                state = "1"
        elif state == "2824":
            if c in ("i", "I"):
                state = "29"
            elif c in ("t", "T"):
                state = "25"
            else:
                state = "1"
        elif state == "30":
            if c in ("e", "E"):
                state = "31"
            else:
                state = "1"
        elif state == "31":
            words["site"] += 1
            words['site-positions'].append(position - 3)
            if c in ("w", "W"):
                state = "1251219"
            elif c in ("e", "E"):
                state = "136"
            elif c in ("s", "S"):
                state = "28"
            elif c in ("p", "P"):
                state = "32"
            else:
                state = "1"
        elif state == "34":
            if c in ("e", "E"):
                state = "35"
            else:
                state = "1"
        elif state == "35":
            words['page'] += 1
            words['page-positions'].append(position - 3)
            if c in ("w", "W"):
                state = "1251219"
            elif c in ("e", "E"):
                state = "136"
            elif c in ("s", "S"):
                state = "28"
            elif c in ("p", "P"):
                state = "32"
            else:
                state = "1"
        elif state == "3017":
            if c in ("e", "E"):
                state = "3118"
            else:
                state = "1"
        elif state == "3118":
            words['website'] += 1
            words['site'] += 1
            words['website-positions'].append(position - 6)
            words['site-positions'].append(position - 3)
            if c in ("w", "W"):
                state = "1251219"
            elif c in ("e", "E"):
                state = "136"
            elif c in ("s", "S"):
                state = "28"
            elif c in ("p", "P"):
                state = "32"
            else:
                state = "1"
        elif state == "3410":
            if c in ("e", "E"):
                state = "3511"
            else:
                state = "1"
        elif state == "3511":
            words['webpage'] += 1
            words['page'] += 1
            words['webpage-positions'].append(position - 6)
            words['page-positions'].append(position - 3)
            if c in ("w", "W"):
                state = "1251219"
            elif c in ("e", "E"):
                state = "136"
            elif c in ("s", "S"):
                state = "28"
            elif c in ("p", "P"):
                state = "32"
            else:
                state = "1"
        elif state == "25":
            if c in ("e", "E"):
                state = "26"
            else:
                state = "1"
        elif state == "26":
            if c in ("r", "R"):
                state = "27"
            else:
                state = "1"
        elif state == "27":
            words['webmaster'] += 1
            words['webmaster-positions'].append(position - 8)
            if c in ("w", "W"):
                state = "1251219"
            elif c in ("e", "E"):
                state = "136"
            elif c in ("s", "S"):
                state = "28"
            elif c in ("p", "P"):
                state = "32"
            else:
                state = "1"

        try:
            record_file.write("f({}, '{}') -> {}\n".format(prev_state, c, state))
        except:
            continue
        finally:
            prev_state = state

    print_results(result_file, words)

    record_file.close()
    result_file.close()

# Buscador de palabras
# La función se encarga de obtener los caracteres del archivo de texto
# que se desea analizar o el contenido de una pagina web, para posteriormente
# ingresarla al automata y encontrar las coincidencias
def word_finder():
    os.system("clear")
    file_direction = input("Introduzca el nombre del archivo o la URL a analizar: ")

    if file_direction[:4] == "http":
        try:
            html = urllib.request.urlopen(file_direction).read().decode('utf-8')
            text = get_text(html)
        except urllib.error.URLError as e:
            os.system("clear")
            print("Se fallo al conectarse con el servidor.")
            print("Razon: ", e.reason, "\n")
            return
    else:
        file = open(file_direction, "r")
        text = file.read()

    DFA_word_finder(text)

    os.system("clear")
    print("Busqueda terminada!")


# Grafico del grafico del automata
# La funcion permite visualizar de forma grafica al automata
def graph_automata():
    d = graphviz.Digraph('2')
    d.attr(rankdir='LR')

    d.attr('node', shape='circle')
    d.node('1')

    d.attr('node', shape='doublecircle')
    d.node('137471421')

    d.attr('node', shape='plaintext')
    d.edge('', '1', label='Inicio')

    d.attr('node', shape='circle')
    d.edge('1', '1', label='Σ - w - e - p - s')
    d.edge('1', '1251219', label='w')
    d.edge('1', '136', label='e')
    d.edge('1', '28', label='s')
    d.edge('1', '32', label='p')

    d.edge('1251219', '1', label='Σ - w - e - p - s')
    d.edge('1251219', '1251219', label='w')
    d.edge('1251219', '136361320', label='e')
    d.edge('1251219', '28', label='s')
    d.edge('1251219', '32', label='p')

    d.edge('136', '1', label='Σ - w - e - p - s - b')
    d.edge('136', '1251219', label='w')
    d.edge('136', '136', label='e')
    d.edge('136', '137', label='b')
    d.edge('136', '28', label='s')
    d.edge('136', '32', label='p')

    d.edge('28', '1', label='Σ - i')
    d.edge('28', '29', label='i')

    d.edge('32', '1', label='Σ - a')
    d.edge('32', '33', label='a')

    d.edge('136361320', '1', label='Σ - w - e - p - s')
    d.edge('136361320', '137471421', label='b')
    d.edge('136361320', '1251219', label='w')
    d.edge('136361320', '136', label='e')
    d.edge('136361320', '28', label='s')
    d.edge('136361320', '32', label='p')

    d.edge('29', '1', label='Σ - t')
    d.edge('29', '30', label='t')

    d.edge('33', '1', label='Σ - g')
    d.edge('33', '34', label='g')

    d.edge('137471421', '1', label='Σ - w - e - p - s - a - m')
    d.edge('137471421', '1251219', label='w')
    d.edge('137471421', '136', label='e')
    d.edge('137471421', '2815', label='s')
    d.edge('137471421', '328', label='p')
    d.edge('137471421', '138', label='a')
    d.edge('137471421', '122', label='m')

    d.edge('2815', '1', label='Σ - i')
    d.edge('2815', '2916', label='i')

    d.edge('328', '1', label='Σ - a')
    d.edge('328', '339', label='a')

    d.edge('137', '1', label='Σ - w - e - p - s - a')
    d.edge('137', '1251219', label='w')
    d.edge('137', '136', label='e')
    d.edge('137', '28', label='s')
    d.edge('137', '32', label='p')
    d.edge('137', '138', label='a')

    d.edge('122', '1', label='Σ - w - e - p - s - a')
    d.edge('122', '1251219', label='w')
    d.edge('122', '136', label='e')
    d.edge('122', '28', label='s')
    d.edge('122', '32', label='p')
    d.edge('122', '123', label='a')

    d.edge('2916', '1', label='Σ - t')
    d.edge('2916', '3017', label='t')

    d.edge('339', '1', label='Σ - g')
    d.edge('339', '3410', label='g')

    d.edge('138', '1', label='Σ - w - e - p - s - y')
    d.edge('138', '1251219', label='w')
    d.edge('138', '136', label='e')
    d.edge('138', '28', label='s')
    d.edge('138', '32', label='p')

    d.edge('123', '1', label='Σ - w - e - p - s')
    d.edge('123', '1251219', label='w')
    d.edge('123', '136', label='e')
    d.edge('123', '2824', label='s')
    d.edge('123', '32', label='p')

    d.edge('139', '1', label='Σ - w - e - p - s')
    d.edge('139', '1251219', label='w')
    d.edge('139', '136', label='e')
    d.edge('139', '28', label='s')
    d.edge('139', '32', label='p')

    d.edge('2824', '1', label='Σ - i - t')
    d.edge('2824', '29', label='i')
    d.edge('2824', '25', label='t')

    d.edge('25', '1', label='Σ - e')
    d.edge('25', '26', label='e')

    d.edge('26', '1', label='Σ - r')

    d.attr('node', shape='doublecircle')

    d.edge('26', '27', label='r')

    d.edge('27', '1', label='Σ - w - e - s - p')
    d.edge('27', '1251219', label='w')
    d.edge('27', '136', label='e')
    d.edge('27', '28', label='s')
    d.edge('27', '32', label='p')

    d.edge('138', '139', label='y')

    d.edge('30', '1', label='Σ - e')
    d.edge('30', '31', label='e')
    d.edge('31', '1', label='Σ - w - e - p - s')
    d.edge('31', '1251219', label='w')
    d.edge('31', '136', label='e')
    d.edge('31', '28', label='s')
    d.edge('31', '32', label='p')

    d.edge('34', '1', label='Σ - e')
    d.edge('34', '35', label='e')
    d.edge('35', '1', label='Σ - w - e - p - s')
    d.edge('35', '1251219', label='w')
    d.edge('35', '136', label='e')
    d.edge('35', '28', label='s')
    d.edge('35', '32', label='p')

    d.edge('3017', '1', label='Σ - e')
    d.edge('3017', '3118', label='e')
    d.edge('3118', '1', label='Σ - w - e - p - s')
    d.edge('3118', '1251219', label='w')
    d.edge('3118', '136', label='e')
    d.edge('3118', '28', label='s')
    d.edge('3118', '32', label='p')

    d.edge('3410', '1', label='Σ - e')
    d.edge('3410', '3511', label='e')

    d.edge('3511', '1', label='Σ - w - e - p - s')
    d.edge('3511', '1251219', label='w')
    d.edge('3511', '136', label='e')
    d.edge('3511', '28', label='s')
    d.edge('3511', '32', label='p')

    d.render('DFA', view=True)

    os.system("clear")
