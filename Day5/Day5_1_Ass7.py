lst=[]
while True:
    n=int(input("Enter a No: "))
    d=n%10
    if d>=len(lst):
        for i in range(d-len(lst)):
            lst.append([])
        lst.append([n])
    else:
        lst[d].append(n)
    ch=input("Do you want to add more no?(y/n) ")
    if ch!='y':
        break
print(lst)