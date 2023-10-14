s1=input("Enter string: ")
s2=input("Enter string: ")
s=""
c=len(s2)-1
for i in s1:
    s=s+i
    s=s+s2[c]
    c-=1
print(s)
