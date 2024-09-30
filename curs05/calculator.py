"""
2 valori introduse de la tastatura si operatia
"""


def validare_numar(a):
    numar = input(f"Te rog introdu o valoare pentru valoarea {a}:")
    while numar.isdigit() is False:
        numar = input(f"Te rog reintrodu un input pentru valoarea {a} : ")
    return int(numar)


def validare_operand():
    operatie = input(f"Operatorul este : ")
    while operatie not in "+-*/":
        operatie = input(f"Te rog sa alegi unul din urmatoarele semne + - / * : ")
    return operatie


def suma(oper1, oper2, operand):
    if operand == "+":
        return oper1 + oper2
    elif operand == "-":
        return oper1 - oper2
    elif operand == "/":
       while oper2 ==0:
           oper2=validare_numar(2)
       return oper1 / oper2
    else:
        return oper1 * oper2


operator1 = validare_numar(1)
operator2 = validare_numar(2)
operand = validare_operand()

print(suma(operator1, operator2, operand))
