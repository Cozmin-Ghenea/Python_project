tabla = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}

# afisare tabla
def afisare_tabla(tabla):
    print(f"{tabla[1]} | {tabla[2]} | {tabla[3]}\n---------\n{tabla[4]} | {tabla[5]} | {tabla[6]}\n---------\n{tabla[7]} | {tabla[8]} | {tabla[9]}")

# verifica daca un jucator a castigat
def verificare_castigator(tabla, semn):
    castig = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # linii
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # coloane
        [1, 5, 9], [3, 5, 7]  # diagonale
    ]
    for combinatie in castig:
        if tabla[combinatie[0]] == tabla[combinatie[1]] == tabla[combinatie[2]] == semn:
            return True
    return False

# locurile libere
def locuri_libere(tabla):
    locuri_libere = []
    for k, v in tabla.items():
        if v == '':
            locuri_libere.append(k)
    return locuri_libere




#inputul utilizator
def mutare_jucator(tabla):
    pozitie = int(input("Alege o pozitie (1-9): "))
    while pozitie not in locuri_libere(tabla):
        pozitie = int(input("Pozitie invalida. Alege alta pozitie (1-9): "))
    tabla[pozitie] = 'X'



# verificarea si blocarea
def verifica_si_blocheaza_castig(tabla, semn):
    castig = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # linii
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # coloane
        [1, 5, 9], [3, 5, 7]  # diagonale
    ]
    for combinatie in castig:
        valori = [tabla[combinatie[0]], tabla[combinatie[1]], tabla[combinatie[2]]]
        if valori.count(semn) == 2 and '' in valori:  # doua semne la fel si un loc liber
            index_gol = valori.index('')
            tabla[combinatie[index_gol]] = '0'
            return True
    return False

# mutarea calculator
def mutare_calculator(tabla):
    # verificare daca calculatorul castiga
    if verifica_si_blocheaza_castig(tabla, '0'):
        return
    # verificare daca utilizatorul castiga si blocare
    if verifica_si_blocheaza_castig(tabla, 'X'):
        return
    # mutare pe pozitiile favorabile daca nu blocam sau castigam
    pozitii_favorabile = [5, 1, 3, 7, 9, 2, 4, 6, 8]
    for pozitie in pozitii_favorabile:
        if tabla[pozitie] == '':
            tabla[pozitie] = '0'
            return

# rulare joc
def joc():
    while '' in tabla.values():
        afisare_tabla(tabla)

        # mutare jucator
        mutare_jucator(tabla)
        if verificare_castigator(tabla, 'X'):
            afisare_tabla(tabla)
            print("Jucatorul a castigat!")
            return

        # mutare calculator
        mutare_calculator(tabla)
        if verificare_castigator(tabla, '0'):
            afisare_tabla(tabla)
            print("Calculatorul a castigat!")
            return

    # remiza
    afisare_tabla(tabla)
    print("Remiza!")


# main
joc()