class MenuInteractif:
    def __init__(self):
        pass

    def lancer(self):
        while True:
            choix = input("1: Bonjour, 2: Addition, 0: Quitter → ")
            if choix == "1":
                print("Bonjour")
            elif choix == "2":
                a = float(input("a = "))
                b = float(input("b = "))
                print("Somme :", a + b)
            elif choix == "0":
                print("Au revoir !")
                break
            else:
                print("Option invalide")

if __name__ == "__main__":
    MenuInteractif().lancer()
