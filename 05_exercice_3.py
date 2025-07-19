class InverserChaine:
    def __init__(self, chaine):
        self.chaine = chaine
    def inverser(self):
        inv = ''.join(reversed(self.chaine))
        print(f"Chaîne inversée : {inv}")
if __name__ == "__main__":
    chaine = input("Chaine : ")
    obj = InverserChaine(chaine)
    obj.inverser()
