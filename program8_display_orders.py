import mysql.connector

connection = mysql.connector.connect(
    host="localhost", user="root", password="Suhana@1204",
    database="Sales_customers_database_management"
)
cursor = connection.cursor()

cursor.execute("SELECT onum, odate, oamount, cnum, snum FROM orders ORDER BY onum")
records = cursor.fetchall()

print("\nORDER DETAILS")
print("-" * 80)
for row in records:
    print("Order:", row[0], "| Date:", row[1], "| Amount:", row[2],
          "| Customer:", row[3], "| Salesperson:", row[4])

cursor.close()
connection.close()
