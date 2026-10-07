import mysql.connector

connection = mysql.connector.connect(
    host="localhost", user="root", password="YOUR_PASSWORD",
    database="Sales_customers_database_management"
)
cursor = connection.cursor()

sql = "SELECT * FROM customer WHERE city IN ('London', 'Bengaluru', 'Paris', 'Mumbai')"
cursor.execute(sql)
records = cursor.fetchall()

print("\nCUSTOMERS FROM SELECTED CITIES")
print("-" * 60)
for row in records:
    print("Customer Number:", row[0], "| Name:", row[1],
          "| City:", row[2], "| Salesperson:", row[3])

cursor.close()
connection.close()
