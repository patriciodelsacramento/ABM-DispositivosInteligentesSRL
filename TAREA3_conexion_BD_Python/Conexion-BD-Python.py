import mysql.connector
midb = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="proyectointegradorv01"
)
print(midb)
