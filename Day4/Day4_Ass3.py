s=input("Enter a Phrase")
s1=""
'''for i in s:
    if i not in ['?','.','!'," ","'",',']:
        s1=s1+i.lower()
if s1==s1[::-1]:
    print(f"Phrase is Palindrome")
else:
    print(f"Phrase is not Palindrome")'''

for i in s:
    if i.isalpha():
        s1=s1+i.lower()
if s1==s1[::-1]:
    print(f"Phrase is Palindrome")
else:
    print(f"Phrase is not Palindrome")
