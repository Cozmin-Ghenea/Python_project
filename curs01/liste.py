lista = [8, 2, 8, 'Ana are creat ',False,-2, 4.2, True]

# print(lista[6:7])
# print(len(lista))

# print(lista[2:]) => va merge pana la finalul listei
# print(lista[2:4]) => [8, 'Ana are creat ']
# print(lista[2:8]) => [8, 'Ana are creat ', 4.2, True]
# print(lista[-1]) => True
# print(lista[-6]) => 8
# print(lista[-6:]) => [8, 2, 8, 'Ana are creat ', 4.2, True]
# print(lista[-6:-3]) => [8, 2, 8]
# print(lista[2: 8: 2]) => [8, 4.2] va sari din 2 in 2
lista.append(5.6)
# lista.remove(2)
lista.pop(3)
# lista.clear()
# lista.reverse()
lista.sort() #[-2, False, True, 2, 4.2, 5.6, 8, 8]
print(lista)
# print(lista.index(8))