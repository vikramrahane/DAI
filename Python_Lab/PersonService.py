from PersonClass import *
empdetails={}
def addnewemployee(ch):
    
    enm=input("Enter Name: ")
    mob=input("Enter Mobile: ")
    
    dt=input("Enter Department: ")
    ds=input("Enter Designation: ")
    if ch==1:
        s=float(input("Enter Salary: "))
        ob=SalariedEmp(enm,mob,dt,ds,s)
    else:
        charg=input("Enter Charges: ")
        hrs=input("Enter Hours: ")
        ob=ContractEmp(enm,mob,dt,ds,charg,hrs)
    empdetails[ob.get_pid()]=ob
def displayall():
    for v in empdetails.values()    :
        print(v)
def deleteempbyid(eid):
    v=empdetails.get(eid,-1)
    if v!=-1:
        choice=input("Do you really want to delete?(y/n) ")
        if choice=='y':
            empdetails.pop(eid)
            return 1
        else:
            return 2
    else:
        return 3
def modifydetails(eid,s=0,charges=1):
    v=empdetails.get(eid,-1)
    if v!=-1:
        choice=input("Do you really want to modify?(y/n) ")
        if choice=='y':
            if isinstance(v, SalariedEmp):
                v.set_sal(s)
                return 1
            elif isinstance(v, ContractEmp):
                v.set_hrs(s)
                v.set_charg(charges)
                return 1
        else:
            return 2
    else:
        return 3
def calnetsal(eid):
    v=empdetails.get(eid,-1)
    if v!=-1:
        return v.calculatesal()
    else:
        return v
def findbytype(etype):
    lst=[]
    if etype==1:
        for v in empdetails.values():
            if isinstance(v, SalariedEmp):
                lst.append(v)
    elif etype==2:
        for v in empdetails.values():
            if isinstance(v, ContractEmp):
                lst.append(v)
    if len(lst)>0:
        return lst
    else:
        return None
def findbysal(sal):
    lst=[]
    for v in empdetails.values():
        if isinstance(v, SalariedEmp):
            if float(v.get_sal())>sal:
                lst.append(v)
        elif isinstance(v, ContractEmp):
            if float(v.get_charg())>sal:
                lst.append(v)
        else:
            pass
    if len(lst)>0:
        return lst
    else:
        return None