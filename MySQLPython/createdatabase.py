import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="admin"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")