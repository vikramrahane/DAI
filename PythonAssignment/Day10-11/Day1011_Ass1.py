import sqlite3

try:
    con=sqlite3.connect("employee.db")
    print("Connection Done.")
except:
    print("Not Connected")
    
def displayall():
    cursor.execute("select * from employee")
    for row in cursor.fetchall(): #it return row as tuple
        print(f"eid: {row[0]}, ename: {row[1]}, Salary: {row[2]}, Mob No: {row[3]}")

def addnewemp():
    try:
        eid=int(input("Enter employee ID: "))
        ename=input("Enter employee Name: ")
        sal=float(input("Enter employee Salary: "))
        mob=input("Enter employee Mobile No: ")
        query=f"insert into employee values({eid},'{ename}',{sal},{mob})"
        #print(sql)
        cursor.execute(query)
        #cursor.execute("insert into product values(?,?,?,?)",(pid,pname,qty,price))
        con.commit()
    except:
        print("Error Occure")
        con.rollback()
    
def displaybyid(eid):
    try:
        #cursor.execute("select * from product where pid=?",(pid,)) # we give tuple for ? values      
        cursor.execute(f"select * from employee where eid={eid}")
        row=cursor.fetchone()
        if row!=None:
            print(f"eid: {row[0]}, ename: {row[1]}, Salary: {row[2]}, Mob No: {row[3]}")
        else:
            print("NOt Found")
    except:
        print("Error Occure")
        
def deletebyid(eid):
    try:
        cursor.execute(f"select * from employee where eid={eid}")
        row=cursor.fetchone()
        if row!=None:
            cursor.execute(f"delete from employee where eid={eid}")
            con.commit()
            return True
        else:
            return False
        
        #cursor.execute("delete from product where pid=?",(pid,))
        
        
    except:
        print("Error Occure")
        con.rollback()
        return False
def updatebyid(eid,ename,sal,mob):
    try:
        cursor.execute(f"select * from employee where eid={eid}")
        row=cursor.fetchone()
        if row!=None:
            cursor.execute(f"update employee set ename='{ename}',sal={sal},mob={mob} where eid={eid}")
            #cursor.execute("update product set pname=?, qty=?,price=? where pid=?",(pname,qty,price,pid))
            con.commit()
            return True
        else:
            return False
    except:
        print("Error Occure")
        con.rollback()
        return False
def displaybysal(sal):
    cursor.execute("select * from employee")
    for row in cursor.fetchall(): #it return row as tuple
        if row[2]>sal:
            print(f"eid: {row[0]}, ename: {row[1]}, Salary: {row[2]}, Mob No: {row[3]}")
cursor=con.cursor()

ch=0
while ch!=7:
    ch=int(input("""
    1. add new employee
    2. delete employee by id
    3. update by id
    4. display all
    5. display by id
    6. display all employee with sal > given sal 
    7. Exit
    CHoice: """))
    match ch:
        case 1:
            addnewemp()
        case 2:
            pid=int(input("Enter Employee ID: "))
            status=deletebyid(pid)
            if status:
                print("Delete Successfully")
            else:
                print("not Found")
        case 3:
            eid=int(input("Enter Employee ID: "))
            ename=input("Enter Employee NAme: ")
            sal=float(input("Enter Employee Salary: "))
            mob=input("Enter Employee Mobile No: ")
            status=updatebyid(eid,ename,sal,mob)
            if status:
                print("Updated Successfully")
            else:
                print("not Found")
        case 4:
            displayall()
        case 5:
            eid=int(input("Enter Employee ID: "))
            displaybyid(eid)
        case 6:
            sal=float(input("Enter Salary: "))
            displaybysal(sal)
        case 7:
            print("Thank you for visiting.")
            con.close()