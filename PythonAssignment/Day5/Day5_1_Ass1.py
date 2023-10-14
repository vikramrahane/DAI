import sys
str=input("Enter a String: ")
while True:
    print('''1. Char Even Pos
            2. Char odd Pos
            3. Length of String
            4. add 'a' len times
            5. Exit''')
    ch=int(input("Enter a Choice: "))
    if ch==1:
        print("Characters at Even Position: ",str[0::2])
    elif ch==2:
        print("Characters at Odd Position: ",str[1::2])
    elif ch==3:
        print("Length of String: ",len(str))
    elif ch==4:
        s=str+"a"*len(str)
        print(s)
    elif ch==5:
        sys.exit()
    else:
        print("Wrong Choice")
