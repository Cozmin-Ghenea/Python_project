"""
Se cer 2 nr intregi de la tastatura. Sa se calculeze produsul daca produsul dintre cele 2 numere este
mai mic sau egal cu 1000, altfel, sa se returneze suma acestora.""
"""

nr1 = input("Primul numar este : ")
nr2 = input("Al doilea numar este : ")
rezul = None
semn = None
if nr1.isdigit() and nr2.isdigit():
    nr1 = int(nr1)
    nr2 = int(nr2)
    if nr1 * nr2 <= 1000:
        rezul = nr1 * nr2
        semn = "Inmultirii"
    else:
        rezul = nr1 + nr2
        semn = "Adunarii"
else:
    print("Nu ati ales numere")

print(f"Rezultatul {semn} este {rezul}")
