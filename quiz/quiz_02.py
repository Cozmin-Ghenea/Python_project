cnp = 1221010170021
if len(str(cnp))!=13:
    print("CNP Invalid")

arr = [int(x) for x in str(cnp)]
arr_control =  [int(x) for x in str(2791463582790)]
s   = "".join(str(x) for x in arr[0:1])
s_control = "".join(str(x) for x in arr_control[0:1])
aa  = "".join(str(x) for x in arr[1:3])
aa_control = "".join(str(x) for x in arr_control[1:3])
ll  = "".join(str(x) for x in arr[3:5])
ll_control = "".join(str(x) for x in arr_control[3:5])
zz  = "".join(str(x) for x in arr[5:7])
zz_control = "".join(str(x) for x in arr_control[5:7])
jj  = "".join(str(x) for x in arr[7:9])
jj_control = "".join(str(x) for x in arr_control[7:9])
nnn = "".join(str(x) for x in arr[9:12])
nnn_control = "".join(str(x) for x in arr_control[9:12])
c   = "".join(str(x) for x in arr[12:13])
c_control=0

for i,v in enumerate(arr):
    if i == len(arr):
        continue
    c_control += arr[i] * arr_control[i]
if int(s)==0:
    print("CNP Invalid")
elif int(s)==7 or int(s)== 8 or int(s) == 9: #cerinta extrem de ciudata
    aa = int(aa) + 1
    if aa==100:
        aa="00"
elif int(ll)>13:
    print("CNP Invalid")
elif int(zz)>32:
    print("CNP Invalid")
elif int(jj)>53:
    print("CNP Invalid")
elif c_control%11 == 10 and int(c)!=1:
    print("CNP Invalid -> Pasul C=1 ")
elif int(c)!=c_control%11 and c_control%11 != 10:
    print("CNP Invalid -> Pasul C-2")
else:
    print(f"CNP-ul {cnp} este valid")

