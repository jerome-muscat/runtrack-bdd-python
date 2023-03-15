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
        ajout_req = f"insert into employes (nom, prenom, salaire, id_service) \
            \nvalues ('{nom}', '{prenom}', {salaire}, {id_service})"
        self.cursor.execute(ajout_req)
        self.bd.commit()
        self.close()

    def lecture(self):
        self.connect()
        lecture_req = "select * from employes"
        self.cursor.execute(lecture_req)
        resultat = self.cursor.fetchall()
        self.close()
        return resultat

    def lectureCondition(self, condition):
        self.connect()
        if type(condition) == str:
            lecture_cond_req = f"select * from employes where {condition}"
            self.cursor.execute(lecture_cond_req)
            resultat = self.cursor.fetchall()
            self.close()
            return resultat
        else:
            print("Erreur, condition pas en str")

    def maj(self, champ, nouvelle_valeur, condition):
        self.connect()
        if type(champ) != str:
            print("Le format du champ n'est pas en str")
        
        elif type(condition) != str:
            print("Le format de condition n'est pas en str")
        
        else:
            maj_req = f"update employes set {champ} = {nouvelle_valeur} where {condition}"
            self.cursor.execute(maj_req)
            self.bd.commit()
            self.close()

    def supr(self, condition):
        self.connect()
        if type(condition) == str:
            supr_req = f"delete from employes where {condition}"
            self.cursor.execute(supr_req)
            self.bd.commit()
            self.close()
            
        else:
            print("Le format de condition, n'est pas en str")

employes = Employes('localhost', 'root', 'root', 'magasin')

list_employes = employes.lecture()
for employe in list_employes:
    print(employe)

employes.ajout('Le Coz', 'Tara', 15000, 1)

list_employes = employes.lecture()
for employe in list_employes:
    print(employe)

list_employes = employes.lectureCondition('salaire > 3000')
for employe in list_employes:
    print(employe)

employes.maj('salaire', 4000, 'id = 3')

employes.supr('id = 10')
employes.supr('id = 11')

list_employes = employes.lecture()
for employe in list_employes:
    print(employe)