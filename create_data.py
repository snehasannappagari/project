import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='9908825568')
print(mydb.connection_id)
cur=mydb.cursor()
cur.execute("create database InventoryManagement_5")