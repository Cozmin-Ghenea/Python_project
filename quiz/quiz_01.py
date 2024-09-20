"""
1. Sa se verifice daca textul introdus de la tastatura de catre un utilizator este un sir de
caractere de tip string sau un sir de numere. Utilizati instructiunea de tip if-elif-else.
In cazul in care valoarea este un sir de caractere, afisati pe ecran mesajul “Sirul de
caractere a fost gasit de Mihai”, unde Mihai reprezinta numele vostru preluat automat de la tastatura.
"""
text = input("Te rog introdu ceva: ")
if text.isnumeric():
    print("Ati introdus un un sir de caractere de tip numeric ")
elif type(text)==str:
    print(f'Sirul de caractere a fost gasit de {text}')
else:
    print("Mesaj default")
"""
2. Creati un program in care utilizatorul sa introduca un numar. Validati daca acest
numar este par sau impar si afisati un raspuns in acest sens.
"""
nr = input("Te rog introdu un numar: ")
if nr.isnumeric():
    nr=int(nr)
    if nr % 2 ==0:
        print(f"{nr} este par")
    elif nr%2 ==1:
        print(f"{nr} este impar")
else:
    print(f"{nr} nu este un numar din pacate")
"""
Creati un program in care utilizatorul sa introduca un an. Calculati daca anul este
bisect sau nu si afisati un raspuns in acest sens. OBS. Un an bisect se imparte exact la 4 (fara rest)
"""
an = input("Te rog introdu un an: ")
if an.isnumeric():
    an=int(an)
    if an % 4 == 0:
        print(f"{an} este un an bisect")
    else:
        print(f"{an} nu este un an bisect")
else:
    print(f"{an} nu este un numar valid din pacate")
"""
Creati un program in care utilizatorul sa introduca un numar. Calculati daca numarul
este pozitiv, zero sau negativ. In cazul in care este pozitiv validati daca este mai mic
decat 10 si afisati un mesaj de confirmare..Daca numarul este zero afisati “Numarul
este 0”, iar daca numarul este negativ atunci transformati numarul in numar pozitiv si
afisati numarul pozitiv.
"""
num = input("Te rog introdu un numar: ")
num = int(num)
if 0 < num < 10:
    print(f"{num} este mai mare decat 0 dar mai mic decat 10")
elif num> 10:
    print(f"{num} este mai mare decat 0 si mai mare decat 10")
elif num == 0:
    print("Numarul este 0")
elif num < 0:
    print(f"{num} este un numar negativ dar ti l-am facut pozitiv aici : {-num}")
"""
Creati un program care are ca scop un meniu. Meniul se va selecta prin introducerea
de la tastaura a unui numar intre 1 si 5 captat intr-o variabila. Prezentati prin afisare
acest sir de caractere:
“””
 1 – Afisare lista de cumparaturi
2 – Adaugare element
3 – Stergere element
4 – Sterere lista de cumparaturi
5 - Cautare in lista de cumparaturi “””
Apoi folosindu-va de o constructie if-elif-else afisati: - daca utilizatorul scrie de la
tastaura 1 afisati “Afisare lista de cumparaturi” - daca utilizatorul scrie de la tastaura 2
afisati “Adugare element” - daca utilizatorul scrie de la tastaura 3 afisati “Stergere
element” - daca utilizatorul scrie de la tastaura 4 afisati “Sterere lista de cumparaturit”
- daca utilizatorul scrie de la tastaura 5 afisati “Adaugare element” - daca utilizatorul
scrie altceva de la tastaura afisati “Alegerea nu exista. Reincercati”
"""

print("””\n1 – Afisare lista de cumparaturi\n2 – Adaugare element\n3 – Stergere element\n4 – Sterere lista de cumparaturi\n5 - Cautare in lista de cumparaturi \n””")
choice = input("Te rog sa alegi un numar de la 1 la 5: ")
if choice == "1":
    print("Afisare lista de cumparaturi")
elif choice == "2":
    print("Adaugare element")
elif choice == "3":
    print("Stergere element")
elif choice == "4":
    print("Sterere lista de cumparaturi")
elif choice == "5":
    print("Cautare in lista de cumparaturi")
else:
    print("Alegerea nu exista. Reincercati")