import mysql.connector

bd = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'laplateforme'
    )

cursor = bd.cursor()

req = 'select sum(capacite) from salles'

cursor.execute(req)
datas = cursor.fetchone()[0]
print(f"La capacité de toutes les salles est de : {datas}")
cursor.close()

