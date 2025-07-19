class ProfilUtilisateur:
    def __init__(self, prenom, age, ville, metier):
        self.prenom = prenom
        self.age = age
        self.ville = ville
        self.metier = metier

    def jours_vecus(self):
        jours = self.age * 365
        print(f"Profil : {self.prenom}, {self.age} ans (~{jours} jours), {self.ville}, {self.metier}")
if __name__ == "__main__":
    prenom = input("Prénom : ")
    age = int(input("Âge : "))
    ville = input("Ville : ")
    metier = input("Métier : ")
    utilisateur = ProfilUtilisateur(prenom, age, ville, metier)
    utilisateur.jours_vecus()
