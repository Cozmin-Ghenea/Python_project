def filtrare (x:list) -> list:
    lista_forloop = []
    for i in x:
        if i % 2 ==0:
            lista_forloop.append(i)
    return lista_forloop

lista_1 = [1,2,3,4,5,6,7,8,9,0,10,111,12,13]
lista_2= list(filter(lambda x:x % 2 == 0, lista_1))
print(lista_2)