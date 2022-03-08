import sqlite3
connection=sqlite3.connect("product.db")


connection.execute('''CREATE TABLE PRODUCTDATA(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
PRODUCTCODE INTEGER,
PRODUCTNAME TEXT,
DISTRIBUTOR TEXT,
PRICE INTEGER,
MANUFACTURER_NAME TEXT);
''')
print("Table created successfully Ramya!!!!!")
getcode=input("Enter productcode: ")
getName=input("Enter name: ")
getdname=input("Enter distributorName: ")
getPrice=input("Enter productPrice: ")
getmfname=input("Enter manufacturename: ")
connection.execute("INSERT INTO PRODUCTDATA(PRODUCTCODE,PRODUCTNAME,DISTRIBUTOR,PRICE,MANUFACTURER_NAME)\
                   VALUES("+getcode+",'"+getName+"','"+getdname+"',"+getPrice+",'"+getmfname+"')")
connection.commit()
connection.close()
print("success!")