"""
Scrieti un program care sa faca split dupa al n-lea element intr-o lista:

lista_start = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
n = 3
result = [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
"""
lista_start = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
n = 3
result = []
a = len(lista_start)

for i in range(n):
    j = []
    for k in range(a):
        if k % n - i == 0:
            j.append(lista_start[k])
    result.append(j)

print(result)
