def inmultire_la_2(x):
    return x * 2

lista = [1,5,4,6,8,3,12]
inmultire_la_2 = lambda x: x*2

rezultat = list(map(inmultire_la_2, lista))
print(rezultat)
