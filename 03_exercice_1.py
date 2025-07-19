class VerificateurInscription:
    def __init__(self, age, pays):
        self.age = age
        self.pays = pays
    def verifier(self):
        if self.age >= 18 and self.pays.lower() in ["congo","cameroun"]:
            print("Inscription autorisée")
        else:
            print("Inscription refusée")
if __name__ == "__main__":
    age = int(input("Age : "))
    pays = input("Pays : ")
    obj = VerificateurInscription(age, pays)
    obj.verifier()
