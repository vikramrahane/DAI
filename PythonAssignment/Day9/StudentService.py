from StudentClass import *
studdetails={}
def addnewstud():
    n=input("Enter a Name:")
    m1=int(input("Enter a Marks1:"))
    m2=int(input("Enter a Marks2:"))
    m3=int(input("Enter a Marks3:"))
    ob=Student(n,m1,m2,m3)
    studdetails[ob.get_id()]=ob
def searchbyid(n):
    if n in studdetails.keys():
        return studdetails[n]
    else:
        return -1
def displayall():
    for v in studdetails.values():
        print(v)
def searchbyname(i):
    for v in studdetails.values():        
        if v.get_name()==i:
            return v
    else:
        return -1
def calgpa(i):
    v=searchbyid(i)
    if v!=-1:
        return (1/3)*v.get_m1()+(1/2)*v.get_m2()+(1/4)*v.get_m3()
    else:
        return v