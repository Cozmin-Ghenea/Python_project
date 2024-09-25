"""
Sa da de la tastatura un string. Sa se elimine caracterele din string pornind de la 0 pana la n,
unde n e dat si el de la tastatura,
"""
a = input("Va rog sa introduceti un string: ")
s = input("Va rog sa introduceti un numar: ")
c = ""

if s.isdigit() and  (s := int(s)) and s <= len(a):
    c=a[s:]
    print(f"Rezultatul va fi: {c}")