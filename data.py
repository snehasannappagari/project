import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='9908825568',database="InventoryManagement_5")
cur=mydb.cursor()
cur.execute('''CREATE TABLE manufacture(manufacture_id INTEGER PRIMARY KEY,product_name TEXT,color TEXT,quantity INTEGER,defective_items INTEGER)''')
cur.execute('''CREATE TABLE goods(goods_id INTEGER PRIMARY KEY,manufacture_id INTEGER,manufactured_date DATE,FOREIGN KEY(manufacture_id) REFERENCES manufacture(manufacture_id))''')
cur.execute('''CREATE TABLE purchase(purchase_id INTEGER PRIMARY KEY,purchase_date DATE,purchase_amount INTEGER)''')

cur.execute('''CREATE TABLE sale(sale_id INTEGER PRIMARY KEY,goods_id INTEGER,sale_date DATE,profit_margin INTEGER,FOREIGN KEY(goods_id) REFERENCES goods(goods_id))''')
mydb.commit()
mydb.close()