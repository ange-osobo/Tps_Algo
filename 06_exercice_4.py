class MotDePasseLoop:
    def __init__(self):
        pass

    def verifier(self):
        mdp = ""
        while mdp != "Python2025":
            mdp = input("Mot de passe : ")
        print("Accès accordé")

if __name__ == "__main__":
    MotDePasseLoop().verifier()
