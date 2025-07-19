class VerifMotDePasse:
    def __init__(self, mdp):
        self.mdp = mdp
    def verifier(self):
        cond = len(self.mdp) >= 8 and any(c.isdigit() for c in self.mdp) and any(c.isupper() for c in self.mdp)
        print("Mot de passe valide" if cond else "Mot de passe invalide")
if __name__ == "__main__":
    mdp = input("Mdp : ")
    obj = VerifMotDePasse(mdp)
    obj.verifier()
