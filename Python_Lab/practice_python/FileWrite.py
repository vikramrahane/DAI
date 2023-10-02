with open("new_data.txt","w") as fh:
    ch='y'
    while ch=='y':
        id=int(input("ENter ID: "))
        name=input("ENter NAme: ")
        p=input("ENter Post: ")
        sal=float(input("ENter Salary: "))
        s=str(id)+":"+name+":"+p+":"+str(sal)+"\n"
        
        fh.write(s)
        ch=input("Do you want to add?(y/n) ")