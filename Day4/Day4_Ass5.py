s=input("Enter a text: ")
'''s1=""
for i in s:
    if i.lower() not in 'aeiou ':
        s1=s1+i+"o"+i
    else:
        s1=s1+i
print(s1)'''

s1=""
for i in s:
    if i.isalpha() and i not in 'aeiou':
        s1=s1+i+"o"+i
    else:
        s1=s1+i
print(s1)
