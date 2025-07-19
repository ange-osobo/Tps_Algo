class InverserListe:
    def __init__(self, liste):
        self.liste = liste
    def inverser(self):
        print(self.liste[::-1])
if __name__ == "__main__":
    liste = input('Liste : ')
    obj = InverserListe(liste)
    obj.inverser()
