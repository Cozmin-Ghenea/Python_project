# for i in len(lista)
#     bloc de cod

# for i in [1,2,3]:
#     print(i) # 1, 2, 3

# for i in "ana are mere":
#     print(i)
#
# for index,value in enumerate(1,2,3):
#     print(f"{index}-{value}")
#
# i = 'seara' # nu ar trebui sa avem cazul in care variabila sa fie folosita in for
# lista = [41, 42, 43]
# for i, v in enumerate(lista): # in cazul asta i-ul va lua indexul si v-ul va lua valoarea
#     print(i, v)
# print(i) #aici va ramane cu ultima valoare din cod

# dictionar = {'a': 1, 'b': 2}
# # for i in dictionar.keys(): # a si b
# # for i in dictionar.items(): # a, 1 si b, 2
# for i in dictionar.values(): # 1 si 2
#     print(i)

# var = 'onomatopee'
# var2 = []
# for i in var:
#    if i!=var[0] and i!=var[-1]:
#        var2.append("_")
#    elif i==var[0]:
#        var2.append(var[0])
#    elif i==var[-1]:
#        var2.append(var[-1])
# print(var2)

cuvant = 'onomatopee'
cuvant_de_inlocuit = ""

for i in cuvant:
   if i!=cuvant[0] and i!=cuvant[-1]:
       cuvant_de_inlocuit += "_"
   else:
       cuvant_de_inlocuit += i
print(cuvant_de_inlocuit)
nr_vieti = 3
while cuvant_de_inlocuit != cuvant and nr_vieti !=0:
    caracter_cerut = input("Alege o litera: ")
    print(caracter_cerut)
    if caracter_cerut in cuvant:
        lista_cuvant_de_inlocuit = list(cuvant_de_inlocuit)
        for i,v in enumerate(cuvant):
            if v == caracter_cerut:
             lista_cuvant_de_inlocuit[i] = caracter_cerut
             cuvant_de_inlocuit = "".join(lista_cuvant_de_inlocuit)
    else:
        nr_vieti-=1
        if nr_vieti != 0:
            print(f"Mai ai {nr_vieti} vieti")
    print(cuvant_de_inlocuit)
if(nr_vieti ==0 ):
    print(f"Ai pierdut cuvantul era {cuvant}")
else:
    print("Ai Castigat")
# functia input -> citeste de la tastatura