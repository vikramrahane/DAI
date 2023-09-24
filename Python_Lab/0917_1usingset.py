# Solve it by using set instead of list
import sys
courselst={("DBDA",100),("DAI",40)}  #set
def addnewcourse():
    cname=input("enter course name")
    capacity=int(input("enter capacity"))
    courselst.add((cname,capacity))
    return True
def displayall(lst=courselst):
    for c,d in lst:
        print(f"{c} : {d}")
def searchcourses(searchc):
    lst=set()
    for cname,capa in courselst:
        if capa>searchc:
            lst.add((cname,capa))

    #lst=list(filter(lambda x:x[1]>searchc,courselst))
    return lst
def searchcoursebyname(old):
    for s in courselst:
        if s[0]==old:
            return True
    else:
        return False
def modifybycoursename(old,new):
    for s in courselst:
        if s[0]==old:
            oldcapa=s[1]

    if searchcoursebyname(old):
        ans=input(f"do you really want to modify {old} with {new} ")
        if ans=='y':
            s.remove((old,oldcapa))
            s.add(new,oldcapa)
            return 1
        else:
            return 2
    else:
        return 3
def delbycname(cname):
    status=searchcoursebyname(cname)
    if status:
        ans=input(f"do you really want to delete {cname} ")
        if ans=='y':
            courselst.remove(pos)
            return 1
        else:
            return 2
    else:
        return 3
def modifybycapacity(cname,newcapa):
    pos,cdetails=searchcoursebyname(cname)
    if pos!=-1:
        ans=input(f"do you really want to modify capacity {cdetails[1]} of {cdetails[0]} with {newcapa} ")
        if ans=='y':
            courselst[pos]=(cdetails[0],newcapa)
            return 1
        else:
            return 2
    else:
        return 3
while True:
    ch=int(input("""
    1. add new course
    2. delete the course
    3. modify course capacity
    4. modify course name
    5.display all
    6.display only courses with capacity > given capacity
    7.Exit
    Choice:
    """))
    match ch:
        case 1:
            status=addnewcourse()
            if status:
                print("new course added successfully")
        case 2:
            cname=input("Enter a course name: ")
            status=delbycname(cname)
            if status==1:
                print("Found and Deleted Successfully")
            elif status==2:
                print("Found but not Deleted")
            else:
                print("course name not found")
        case 3:
            cname=input("Enter course name")
            newcapa=int(input("Enter new capacity"))
            status=modifybycapacity(cname,newcapa)
            if status==1:
                print("found and Modification Done")
            elif status==2:
                print("found but not Modify")
            else:
                print("not found")
        case 4:
            oldcourse=input("Enter old course name")
            newcourse=input("Enter new course name")
            status=modifybycoursename(oldcourse,newcourse)
            if status==1:
                print("Found Modification Done")
            elif status==2:
                print("Found but not Modify")
            else:
                print("course name not found")
        case 5:
            displayall()
        case 6:
            searchc=int(input("enter capacity to search courses"))
            lstc=searchcourses(searchc)
            displayall(lstc)
        case 7:
            print("Thank you for visit")
            sys.exit(0)
