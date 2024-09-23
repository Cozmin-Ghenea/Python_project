text = input("Te rog introdu ceva: ")
is_string = False
for i in text:
    if i not in ['0','1','2','3','4','5','6','8','9','10']:
        is_string = True
        break
if is_string is True:
    print(f'Sirul de caractere a fost gasit de {text}')
else:
    print("Sirul este digit")

nr = input("Te rog introdu un numar: ")
if nr.isnumeric():
    nr=int(nr)
    if nr % 2 ==0:
        print(f"{nr} este par")
    elif nr%2 ==1:
        print(f"{nr} este impar")
else:
    print(f"{nr} nu este un numar din pacate")

an = input("Te rog introdu un an: ")
if an.isnumeric():
    an=int(an)
    if an % 4 == 0:
        print(f"{an} este un an bisect")
    else:
        print(f"{an} nu este un an bisect")
else:
    print(f"{an} nu este un numar valid din pacate")


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