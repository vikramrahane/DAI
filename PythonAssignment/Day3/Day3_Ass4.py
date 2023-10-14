s="asGdfDFfggfFffGffDooHH"
l=[]
u=[]
for i in s:
    if i.islower():
        l.append(i)
    else:
        u.append(i)
n=''.join(l+u)
print("arranging characters giving precedence to lowercase letters:")
print(n)
