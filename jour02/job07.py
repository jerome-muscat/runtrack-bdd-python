import mysql.connector

class Employes:

    def __init__(self, hote, utilisateur, mdp, bdd):
        self.hote = hote
        self.utilisateur = utilisateur
        self.mdp = mdp
        self.bdd = bdd

    def connect(self):
        self.bd = mysql.connector.connect(
            host = self.hote,
            user = self.utilisateur,
            password = self.mdp,
            database = self.bdd
        )
        self.cursor = self.bd.cursor()

    def close(self):
        self.cursor.close()
        self.bd.close()

    def ajout(self, nom, prenom, salaire, id_service):
        self.connect()
        sql = f"insert into employes (nom, prenom, salaire, id_service) \
            \nvalues ('{nom}', '{prenom}', {salaire}, {id_service})"
        self.cursor.execute(sql)
        self.bd.commit()
        self.close()

    def lecture(self):
        self.connect()
        sql = "select * from employes"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        self.close()
        return result

    def lectureCondition(self, condition):
        self.connect()
        if type(condition) == str:
            sql = f"select * from employes where {condition}"
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            self.close()
            return result
        else:
            print("Erreur, condition pas en str")

    def maj(self, champ, nouvelle_valeur, condition):
        self.connect()
        if type(champ) != str:
            print("Le format du champ n'est pas en str")
        elif type(condition) != str:
            print("Le format de condition n'est pas en str")
        else:
            sql = f"update employes set {champ} = {nouvelle_valeur} where {condition}"
            self.cursor.execute(sql)
            # self.bd.commit()
            self.close()

    def supr(self, condition):
        self.connect()
        if type(condition) == str:
            sql = f"delete from employes where {condition}"
            self.cursor.execute(sql)
            # self.bd.commit()
            self.close()
        else:
            print("Le format de condition, n'est pas en str")

employes = Employes('localhost', 'root', 'root', 'magasin')

# sélectionner tous les employés
result = employes.lecture()
for row in result:
    print(row)

employes.ajout('Le Coz', 'Tara', 15000, 1)

# sélectionner tous les employés
result = employes.lecture()
for row in result:
    print(row)

# sélectionner les employés dont le salaire est supérieur à 3000
result = employes.lectureCondition('salaire > 3000')
for row in result:
    print(row)

# mettre à jour le salaire d'un employé
employes.maj('salaire', 4000, 'id = 3')

# supprimer un employé
employes.supr('id = 6')
# supprimer un employé
employes.supr('id = 7')

# sélectionner tous les employés
result = employes.lecture()
for row in result:
    print(row)