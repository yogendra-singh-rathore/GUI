import sqlite3

def connect():
    conn=sqlite3.connect("Project.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS data_project(id INTEGER PRIMARY KEY, orderDate text, customerName text, customerDetails text, orderName text, paymentMethod text, paymentStatus text)")
    conn.commit()
    conn.close()

def insert(orderDate,customerName,customerDetails,orderName,paymentMethod,paymentStatus ):
    conn=sqlite3.connect("Project.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO data_project VALUES (NULL,?,?,?,?,?,?)", (orderDate,customerName,customerDetails,orderName,paymentMethod,paymentStatus))
    conn.commit()
    conn.close()

def view():
     conn=sqlite3.connect("Project.db")
     cur=conn.cursor()
     cur.execute("SELECT * FROM data_project")
     rows=cur.fetchall()
     conn.close()
     return rows

def search(orderDate="",customerName="",customerDetails="",orderName="",paymentMethod="",paymentStatus=""):
    conn=sqlite3.connect("Project.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM data_project WHERE orderDate=? or customerName=? or customerDetails=? or orderName=? or paymentMethod=? or paymentStatus=?",(orderDate,customerName,customerDetails,orderName,paymentMethod,paymentStatus))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("Project.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM data_project WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,orderDate,customerName,customerDetails,orderName,paymentMethod,paymentStatus):
    conn=sqlite3.connect("Project.db")
    cur=conn.cursor()
    cur.execute("UPDATE data_project SET  orderDate=?, customerName=?, customerDetails=?, orderName=?, paymentMethod=?, paymentStatus=? WHERE id=?" , (orderDate,customerName,customerDetails,orderName,paymentMethod,paymentStatus,id))
    conn.commit()
    conn.close()

connect()
