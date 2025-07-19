class JeuDevineNombre:
    def __init__(self):
        pass

    def jouer(self):
        import random
        cible = random.randint(1, 100)
        while True:
            dev = int(input("Devinez le nombre (1–100) : "))
            if dev < cible:
                print("Trop petit")
            elif dev > cible:
                print("Trop grand")
            else:
                print("Bravo !")
                break

if __name__ == "__main__":
    JeuDevineNombre().jouer()
