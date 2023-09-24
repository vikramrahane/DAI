import re
mob=input("Enter a Mobile NO: ")
m=re.match("[987]\d{9}$", mob)
if m!=None:
    print("Mobile number is valid")
else:
    print("Not valid")
    
mob=input("Enter a Mobile NO: ")
m=re.match("\+\d{2,4}-[987]\d{9}$", mob)
if m!=None:
    print("Mobile number is valid")
else:
    print("Not valid")
    
email=input("Enter email: ")
m=re.match("\w+@{1}[a-z]*\.{1}[a-z]{2,3}$", email)
if m!=None:
    print("Email is valid")
else:
    print("Not valid")
    
s="This is Home"
m=re.match("\w+\s\w+\s|w+$", s)
if m!=None:
    print("valid")
else:
    print("Not valid")
    
s="This is Home"
m=re.match("^(\w+)\s(\w+)\s\w+$", s)
if m!=None:
    print(m.group(),m.span())
    print(m.group(1),m.span(1))
    print(m.group(2),m.span(2))
    print("valid")
else:
    print("Not valid")
    
    
acc="xxxxx1234xxxxx"
m=re.match("^x{5}(\d{4})x{5}$", acc)
if m!=None:
    print(m.group(1),m.span(1))
    print("Found")
else:
    print("Not Found")

acc="xxxxxxxxxx1234xxxxxxxxxxxxxx"
m=re.match("x*(\d{4})x*$", acc)
if m!=None:
    print(m.group(1),m.span(1))
    print("Found")
else:
    print("Not Found")
    
    
    
    
    
    
    
    
    
    
    
    
    
    