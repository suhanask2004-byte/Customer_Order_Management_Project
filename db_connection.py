import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Suhana@1204",
        database="Sales_customers_database_management"
    )
