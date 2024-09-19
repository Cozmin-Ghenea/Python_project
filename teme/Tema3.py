nr = input("Alege un numar : ")
while not nr.isnumeric():
    print(f"Te rog alege un numar real nu un caracter: {nr}")
    nr = input("Alege un numar : ")
nr = int(nr)
if nr % 3 == 0 and nr % 5 == 0:
    print('FizzBuzz')
elif nr % 3 == 0:
    print('Fizz')
elif nr% 5 == 0:
    print('Buzz')
else:
    print(nr)