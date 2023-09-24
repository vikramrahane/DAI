import sys
course={"DBDA":(100,60),"DAI":(200,40)}
def addnewcourse():
    cname=input("Enter course name: ")
    duration=int(input("Enter course duration: "))
    capacity=int(input("Enter course capacity: "))
    #course.setdefault(cname,(duration,capacity))
    val=course.get(cname,-1)
    if val==-1:
        course[cname]=(duration,capacity)
        return True
    else:
        return False
def displayall(d=course):
    for k,v in d.items():
        print(f"{k}---->{v}")
def dispbycapacity(capa):
    d={}
    for k,v in course.items():
        if v[1]>capa:
            d[k]=v
    if len(d)!=0:
        return d
    return None
def delbycname(cname):
    val=course.get(cname,-1)
    if val!=-1:
        ch=input("Do you really want to delete?(y/n)")
        if ch=='y':
            course.pop(cname)
            return 1
        else:
            return 2
    else:
        return 3
def modifybycapacity(cname,newcapa):
    val=course.get(cname,-1)
    if val!=-1:
        ch=input(f"Do you really want to Modify capacity {val[1]} with {newcapa}(y/n)")
        if ch=='y':
            course[cname]=(val[0],newcapa)
            return 1
        else:
            return 2
    else:
        return 3
def modifybycoursename(oldcourse,newcourse):
    val=course.get(oldcourse,-1)
    if val!=-1:
        ch=input(f"Do you really want to Modify cname {oldcourse} with {newcourse}(y/n)")
        if ch=='y':
            course.pop(oldcourse)
            course[newcourse]=val
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
            else:
                print("Course exists")
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
            capa=int(input("Enter capacity: "))
            data=dispbycapacity(capa)
            if data!=None:
                displayall(data)
            else:
                print("No course found")
        case 7:
            print("Thank you for visit")
            sys.exit(0)

