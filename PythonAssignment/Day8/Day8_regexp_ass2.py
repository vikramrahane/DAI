import re
lst=[]
ch='y'
while ch=='y':
    line=input("Enter a statement: ")
    m=re.match("[0-9]|[a-zA-Z]{2}",line)
    if m!=None:
        lst.append(line)
    ch=input("Do you want to add more?(y/n) ")
for s in lst:
    print(s)