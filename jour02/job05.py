import mysql.connector

bd = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'laplateforme'
    )

cursor = bd.cursor()

req = 'select sum(superficie) from etage'

cursor.execute(req)
datas = cursor.fetchone()[0]
print(f"La superficie de La Plateforme est de {datas} m2")
cursor.close()

