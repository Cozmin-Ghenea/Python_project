text = input("Adauga un numar: " )
try: # -> secventa de cod folosita care pot fi ignorate
    conversie = int(text)
except ValueError: #-> ValueError -> eroarea exacta pe secventa de cod din try
    print("Exceptie")

except Exception: # -> Exceptie generala doar daca a fost gasita alta eroare ca intra pe acest bloc de cod
    print('Another exception')
else: # -> doar daca try-ul functioneaza fara nici o eroare
    print(conversie)
finally: # -> se executa la final folosit de fel ca sa poata fi inchise fisierele deschise in try
    print('se executa si aici')
