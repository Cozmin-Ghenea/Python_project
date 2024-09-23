lista2 = [12,34,23,5,1]
lista = [12,3,56,2,12]

same = False
if len(lista) >1:
    if lista[-1] == lista[0]:
        same = True

if same:
    print("La fel ")
else:
    print("nu sunt La fel ")