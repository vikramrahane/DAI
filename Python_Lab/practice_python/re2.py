#Write a Python program that matches a string that has an a followed by zero or more b's. 
import re
s='Python exercises, PHP exercises, C# exercises'
p='exercises'
m=re.sub('exercises','Language',s,count=2)
if m!=None:
    print(m)
    print(s)

'''for x in re.finditer(p,s):
    print(x.span()[0],x.group())'''