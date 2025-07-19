class ExtraireIndicesPairs:
    def __init__(self, liste):
        self.liste = liste
    def extraire(self):
        print([self.liste[i] for i in range(0, len(self.liste), 2)])
if __name__ == "__main__":
    liste = input('Liste : ')
    obj = ExtraireIndicesPairs(liste)
    obj.extraire()
