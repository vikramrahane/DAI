import re
user=input("Enter Username: ")
m=re.match("[0-9A-Za-z]+$",user)
if m!=None:
    cnt=0
    while cnt<3:
        passw=input("Enter a Password: ")
        m=re.search("^[a-zA-Z][\W{1,}a-zA-Z]{7}$",passw)
        if m!=None:
            print("Welcome to our application.")
            break
        else:
            cnt+=1
    else:
        print("You exceed 3 Attempts.")        
else:
    print("You Enter a wrong Username.")

