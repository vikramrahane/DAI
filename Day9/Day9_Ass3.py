import sys
from FriendClass import *

frndinfo={}
def addnewfrnd():
    fn=input("Enter a First Name:")
    ln=input("Enter a Last Name: " )
    mob=input("Enter a Mobile No: ")
    email=input("Enter a Email: ")
    bdt=input("Enter a Birthdate:")
    addr=input("Enter a Address: ")
    hoblst=[]
    ch='y'
    while ch=='y':
        s=input("Enter a Hobby: ")
        hoblst.append(s)
        ch=input("Do you want to add more hobbies?(y/n) ")
    obj=Friend(fn,ln,hoblst,mob,email,bdt,addr)    
    frndinfo[obj.get_id()]=obj
def displayall():
    for v in frndinfo.values():
        print(v)
        
def searchbyid(n):
    if n in frndinfo.keys():
        return frndinfo[n]
    else:
        return -1
def searchbyname(fn):
    for v in frndinfo.values():
        if v.get_fname()==fn:
            return v
    else:
        return -1
ch='y'
while ch=='y':
    choice=int(input("""
    1. Add New Friend
    2. Display All Friend
    3. Search by id
    4. Search by name
    5. Display all friend with a particular hobby
    6. Exit 
    Choice :"""))
    match choice:
        case 1:
            addnewfrnd()
        case 2:
            displayall()
        case 3:
            i=int(input("Enter Friend ID: "))
            f=searchbyid(i)
            if f!=-1:
                print(f)
            else:
                print("Friend not Found")
        case 4:
            fn=input("Enter Friend's First Name: ")
            status=searchbyname(fn)
            if status!=-1:
                print(status)
            else:
                print("Friend not Found")
        case 5:
            hob=input("Enter Hobby: ")
            for s in lst:
                if hob in s.get_hobby(hob):
                    print(s)
            
        case 6:
            sys.exit(0)
        case _:
            print("Wrong Choice")