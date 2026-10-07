import mysql.connector

connection = mysql.connector.connect(
    host="localhost", user="root", password="YOUR_PASSWORD",
    database="Sales_customers_database_management"
)
cursor = connection.cursor()

customers = [
    (2001, "John", "London", 1003),
    (2002, "Smith", "Bengaluru", 1001),
    (2003, "David", "Paris", 1004),
    (2004, "Emma", "Mumbai", 1002),
    (2005, "Robert", "Bengaluru", 1005),
    (2006, "Sophia", "London", 1008),
    (2007, "Daniel", "Paris", 1009)
]

sql = "INSERT INTO customer (cnum, cname, city, snum) VALUES (%s, %s, %s, %s)"
cursor.executemany(sql, customers)
connection.commit()

print("7 customer records inserted successfully.")
cursor.close()
connection.close()
