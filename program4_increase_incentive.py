import mysql.connector

connection = mysql.connector.connect(
    host="localhost", user="root", password="YOUR_PASSWORD",
    database="Sales_customers_database_management"
)
cursor = connection.cursor()

cursor.execute("UPDATE salespeople SET comm = comm + 1500.55")
connection.commit()

print("Incentive increased by Rs. 1500.55 successfully.")
cursor.close()
connection.close()
