# if(conditie):
#     #blocDeCod
# elif(conditie):
#     #BlockDeCod
# else:
#     #blockDeCod

nr1 = 4
total, salariu = None, "Salariu Mic" # pot fi initializate mai multe variabile pe aceeasi linie
if (nr1 <= 4) and (salariu := "Salariu mare"):
    print(salariu) # poate fi folosit doar in blocul de cod adiacent if-ului
    total = nr1 +1
elif nr1 > 2:
    total = nr1 +2
    print(salariu) # eroare nu o recunoaste in acest elif
else:
    total = None
print(salariu)


