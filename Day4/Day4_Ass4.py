s=input("Enter a Statement")
s1="abcdefghijklmnopqrstuvwxyz"
for i in s1:
    if i not in s:
        print("Given statement is not pangram")
        break
else:
    print("Given statement is pangram")
