class InversionListe:
    def __init__(self, liste):
        self.liste = liste
    def inverser(self):
        inv = self.liste[::-1]
        print('Inverse :', inv)
if __name__ == "__main__":
    liste = input('Liste : ')
    obj = InversionListe(liste)
    obj.inverser()
