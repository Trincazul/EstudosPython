import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="admin",
  database="database"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE pessoas (nome VARCHAR(255), endereco VARCHAR(255))")