import mysql.connector

connection = mysql.connector.connect(
    host="localhost", user="root", password="YOUR_PASSWORD",
    database="Sales_customers_database_management"
)
cursor = connection.cursor()

orders = [
    (3001, "2026-09-01", 25000.00, 2001, 1003),
    (3002, "2026-09-02", 18500.00, 2002, 1001),
    (3003, "2026-09-03", 32000.00, 2003, 1004),
    (3004, "2026-09-04", 15000.00, 2004, 1002),
    (3005, "2026-09-05", 27500.00, 2005, 1005),
    (3006, "2026-09-06", 21000.00, 2006, 1008),
    (3007, "2026-09-07", 36000.00, 2007, 1009),
    (3008, "2026-09-08", 19500.00, 2002, 1001),
    (3009, "2026-09-09", 28000.00, 2005, 1005)
]

sql = "INSERT INTO orders (onum, odate, oamount, cnum, snum) VALUES (%s, %s, %s, %s, %s)"
cursor.executemany(sql, orders)
connection.commit()

print("9 orders inserted successfully.")
cursor.close()
connection.close()
