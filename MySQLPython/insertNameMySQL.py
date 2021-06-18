import MySQLdb

con = MySQLdb.connect(host='localhost',user='root',passwd='',db='testepython')
con.select_db('testepython')

cursor = con.cursor()

nomep = str(input('Digite qual seu nome: '))
print(nomep)

cursor.execute("INSERT INTO testandodois(nome) VALUES(%s)", (nomep))
con.commit()