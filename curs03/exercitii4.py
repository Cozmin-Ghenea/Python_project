cuvant = input("Introduceti un cuvant:")

c = 0
v = 0
h = 0

for i in cuvant:
    if i in '0123456789':
        h +=1
    elif i in "aeiou":
        v += 1
    else:
        c += 1
print(f"numarul total de:  \n - vocale este {v}, \n - si numarul consoane este {c}, \n - is numere {h}")
