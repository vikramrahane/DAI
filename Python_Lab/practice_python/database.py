import sqlite3
con=sqlite3.connect("myDB.db")
cur=con.cursor()
#cur.execute("create table student(id int,sname txt,mark float)")
cur.execute("insert into student values(1,'tyh',88)")
con.commit()
x=cur.execute("select * from student")
for i in x.fetchall():
    print("ID: ",i[0]," NAme :",i[1]," MArks",i[2])
con.close()