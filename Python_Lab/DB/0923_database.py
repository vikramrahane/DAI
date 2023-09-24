import sqlite3

try:
    con=sqlite3.connect("myDB.db")
    print("Connection Done.")
except:
    print("Not Connected")
    
def displayall():
    cursor.execute("select * from product")
    for row in cursor.fetchall(): #it return row as tuple
        print(f"pid: {row[0]}, pname: {row[1]}, Quantity: {row[2]}, Price: {row[3]}")

def addnewproduct():
    try:
        pid=int(input("Enter Product ID: "))
        pname=input("Enter Product NAme: ")
        qty=int(input("Enter Product Quantity: "))
        price=int(input("Enter Product Price: "))
        query=f"insert into product values({pid},'{pname}',{qty},{price})"
        #print(sql)
        cursor.execute(query)
        #cursor.execute("insert into product values(?,?,?,?)",(pid,pname,qty,price))
        con.commit()
    except:
        print("Error Occure")
        con.rollback()
    
def displaybyid(pid):
    try:
        #cursor.execute("select * from product where pid=?",(pid,)) # we give tuple for ? values      
        cursor.execute(f"select * from product where pid={pid}")
        row=cursor.fetchone()
        if row!=None:
            print(f"pid: {row[0]}, pname: {row[1]}, Quantity: {row[2]}, Price: {row[3]}")
        else:
            print("NOt Found")
    except:
        print("Error Occure")
        
def deletebyid(pid):
    try:
        cursor.execute(f"select * from product where pid={pid}")
        row=cursor.fetchone()
        if row!=None:
            cursor.execute(f"delete from product where pid={pid}")
            con.commit()
            return True
        else:
            return False
        
        #cursor.execute("delete from product where pid=?",(pid,))
        
        
    except:
        print("Error Occure")
        con.rollback()
        return False
def updatebyid(pid,pname,qty,price):
    try:
        cursor.execute(f"select * from product where pid={pid}")
        row=cursor.fetchone()
        if row!=None:
            cursor.execute(f"update product set pname='{pname}',qty={qty},price={price} where pid={pid}")
            #cursor.execute("update product set pname=?, qty=?,price=? where pid=?",(pname,qty,price,pid))
            con.commit()
            return True
        else:
            return False
    except:
        print("Error Occure")
        con.rollback()
        return False
cursor=con.cursor()

ch=0
while ch!=6:
    ch=int(input("""
    1. add new product
    2. delete product by id
    3. update by id
    4. display all
    5. display by id
    6. Exit
    CHoice: """))
    match ch:
        case 1:
            addnewproduct()
        case 2:
            pid=int(input("Enter Product ID: "))
            status=deletebyid(pid)
            if status:
                print("Delete Successfully")
            else:
                print("not Found")
        case 3:
            pid=int(input("Enter Product ID: "))
            pname=input("Enter Product NAme: ")
            qty=int(input("Enter Product Quantity: "))
            price=int(input("Enter Product Price: "))
            status=updatebyid(pid,pname,qty,price)
            if status:
                print("Updated Successfully")
            else:
                print("not Found")
        case 4:
            displayall()
        case 5:
            pid=int(input("Enter Product ID: "))
            displaybyid(pid)
        case 6:
            print("Thank you for visiting.")
            con.close()