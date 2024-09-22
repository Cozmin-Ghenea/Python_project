a = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
a_pe_3=[]
for i in a:
    if i%3==0:
        a_pe_3.append(i)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a.sort()
print(a[1:10:2])
print(a[2:10:2])
print(a[2:10:3]) # pentru punctul 3 intr-o lista ordonata
print(a_pe_3) # pentru punctul 3 intr-o lista neordonata
