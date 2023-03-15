import mysql.connector

bd = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'laplateforme'
    )

cursor = bd.cursor()

req = 'select nom, capacite from salles'

cursor.execute(req)
datas = cursor.fetchall()

print(datas)
cursor.close()

