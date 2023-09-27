from flask import Flask,render_template,redirect,request,url_for
import sqlite3

con=sqlite3.connect("myDB.db",check_same_thread=False)
if con!= None:
    print("Connection Done")
    
cursor=con.cursor()


app=Flask(__name__)

@app.route('/')
def home():
    #return "Hello World"
    return render_template("helloworld.html")
@app.route("/products")
def displayallproduct():    
    cursor.execute("select * from product")
    rows=cursor.fetchall()    
    return render_template("displayproduct.html",data=rows)
@app.route('/acceptproduct')
def displayform():
    return render_template("productdata.html")
@app.route('/products/addproduct',methods=['POST'])
def addproduct():
    pid=request.form.get("pid")
    pname=request.form.get("pname")
    qty=request.form.get("qty")
    price=request.form.get("price")
    cursor.execute("insert into product values(:pid,:pname,:qty,:pr)",(pid,pname,qty,price))
    con.commit()
    #return "product"+pname+"  "+pid
    return redirect('/products')
@app.route('delete/<pid>')
def addproduct():
    return True
if __name__=='__main__':
    app.run(debug=True)