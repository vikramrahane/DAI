l=[]
while True:
    s=input("Enter a String: ")
    pos=-1
    for i in l:
        if i[1]==s[1]:
            pos=l.index(i)
    if pos!=-1:
        l.insert(pos+1,s)
    else:
        l.append(s)
    ch=input("Do you want to add more no?(y/n) ")
    if ch!='y':
        break
print(l)