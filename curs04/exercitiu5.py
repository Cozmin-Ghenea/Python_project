"""scrieti un program care sa extraga inversul dintr-un nr.
Exemplu: 7536 trebuie afisati 6 3 5 7"""

n = input("Numarul tau este : ")
rez = ""

# print(n[::-1])
for i in n:
    rez = i + rez
print(rez)