from PersonService import *
ch=0
while ch!=8:
    ch=int(input("""
    1.Add New Employee
    2.Del emp by id
    3.modify sal or chaarges
    4.Display all
    5.calculate net sal by id
    6.display only given type of employee
    7.Display all with sal>given value
    8.exit
    Choice: """))
    match ch:
        case 1:
            choice=int(input("1. Salaried 2. Contract"))
            addnewemployee(choice)
        case 2:
            eid=input("Enter eid: ")
            status=deleteempbyid(eid)
            if status==1:
                print("Deleted Successfully")
            elif status==2:
                print("Found but not deleted")
            else:
                print("Not Found")
        case 3:
            eid=input("Enter eid: ")
            if eid.startswith("S"):
                s=float(input("Enter Salary: "))
                status=modifydetails(eid,s)
            elif eid.startswith("C"):
                hrs=float(input("Enter Hours: "))
                charges=float(input("Enter charges: "))
                status=modifydetails(eid,hrs,charges)
            else:
                pass
            if status==1:
                print("Modify Successfully")
            elif status==2:
                print("Found but not Modified")
            else:
                print("Not Found")
        case 4:
            displayall()
        case 5:
            eid=input("Enter eid: ")
            status=calnetsal(eid)
            if status!=1:
                print(f"Employee ID: {eid} Net Salary: {status}")
            else:
                print("Not Found")
        case 6:
            etype=int(input("1. Salarised Emp 2. Cotract Emp "))
            l=findbytype(etype)
            if l!=None:
                for v in l:
                    print(v)
            else:
                print("Not Found")
        case 7:
            sal=float(input("Enter Salary: "))
            l=findbysal(sal)
            if l!=None:
                for v in l:
                    print(v)
            else:
                print("Not Found")
        case 8:
            pass
        case others:
            print("wrong choice")
    