nr = input("Numarul tau de telefon ")
str = True
if len(nr)==12 and nr[0: 3] == '+40':
    for i in nr[3:]:
        if i not in '0123456789':
            str = False
            break
else:
    str = False

if(str):
    print("nr valid")
else:
    print("nr invalid")