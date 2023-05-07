import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='9908825568',database="InventoryManagement_5")
cur=mydb.cursor()
cur.execute("INSERT INTO manufacture VALUES (1, 'Red Toy Car', 'Red', 50, 2)")
cur.execute("INSERT INTO manufacture VALUES (2, 'Blue Toy Car', 'Blue', 40, 1)")
cur.execute("INSERT INTO manufacture VALUES (3, 'Wooden Chair', 'Brown', 100, 5)")
cur.execute("INSERT INTO manufacture VALUES (4, 'Wooden Table', 'Brown', 20, 1)")
cur.execute("INSERT INTO manufacture VALUES (5, 'White T-Shirt', 'White', 200, 10)")
cur.execute("INSERT INTO goods VALUES (1, 1, '2023-04-28')")
cur.execute("INSERT INTO goods VALUES (2, 1, '2023-04-29')")
cur.execute("INSERT INTO goods VALUES (3, 3, '2023-05-01')")
cur.execute("INSERT INTO goods VALUES (4, 4, '2023-05-03')")
cur.execute("INSERT INTO goods VALUES (5, 5, '2023-05-04')")

cur.execute("INSERT INTO purchase VALUES (1, '2023-04-30', 5000)")
cur.execute("INSERT INTO purchase VALUES (2, '2023-05-02', 8000)")
cur.execute("INSERT INTO purchase VALUES (3, '2023-05-05', 6000)")

cur.execute("INSERT INTO sale VALUES (1, 1, '2023-05-01', 2000)")
cur.execute("INSERT INTO sale VALUES (2, 3, '2023-05-03', 3000)")
cur.execute("INSERT INTO sale VALUES (3, 4, '2023-05-05', 1500)")


mydb.commit()
mydb.close()