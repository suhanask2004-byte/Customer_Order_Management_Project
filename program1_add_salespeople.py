import mysql.connector

connection = mysql.connector.connect(
    host="localhost", user="root", password="Suhana@1204",
    database="Sales_customers_database_management"
)
cursor = connection.cursor()

salespeople = [
    (1001, "Arun", "Bengaluru", 5000.00),
    (1002, "Rahul", "Mumbai", 5500.00),
    (1003, "Priya", "London", 6000.00),
    (1004, "Sneha", "Paris", 4500.00),
    (1005, "Kiran", "Bengaluru", 7000.00),
    (1006, "Anil", "Mumbai", 5200.00),
    (1007, "Neha", "Delhi", 6500.00),
    (1008, "Vikram", "London", 4800.00),
    (1009, "Pooja", "Paris", 5800.00),
    (1010, "Ravi", "Bengaluru", 6200.00)
]

sql = "INSERT INTO salespeople (snum, sname, city, comm) VALUES (%s, %s, %s, %s)"
cursor.executemany(sql, salespeople)
connection.commit()

print("10 salespeople records inserted successfully.")
cursor.close()
connection.close()
