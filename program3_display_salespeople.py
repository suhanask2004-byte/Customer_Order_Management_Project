import mysql.connector

connection = mysql.connector.connect(
    host="localhost", user="root", password="Suhana@1204",
    database="Sales_customers_database_management"
)
cursor = connection.cursor()

cursor.execute("SELECT * FROM salespeople")
records = cursor.fetchall()

print("\nSALESPEOPLE DETAILS")
print("-" * 60)
for row in records:
    print("SNUM:", row[0], "| Name:", row[1], "| City:", row[2], "| Incentive:", row[3])

cursor.close()
connection.close()
