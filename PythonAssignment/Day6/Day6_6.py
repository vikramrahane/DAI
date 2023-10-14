set1=set()
ch='y'
while ch=='y':
    set1.add(input("Enter a string: "))
    ch=input("Do you want to add more strings?(y/n)")
print("set1=",set1)
n=int(input("Enter minimum length of string to display:"))
for s in set1:
    if len(s)>n:
        print(s,end=", ")