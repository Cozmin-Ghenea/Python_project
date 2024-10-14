suma = lambda x,y: x + y
rezultat = suma (1,2)

print(rezultat)

jucatori =[{
    "nume": "Popescu",
    "prenume": "Ion",
    "varsta": 21
    },
    {
    "nume": "Marin",
    "prenume": "Andreea",
    "varsta": 42
    },
]

sortare_valori = sorted(jucatori, key=lambda valoare: valoare['varsta'])

print(sortare_valori)