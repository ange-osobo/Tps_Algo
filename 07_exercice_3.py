class StatistiquesListe:
    def __init__(self, liste):
        self.liste = liste
    def afficher(self):
        print('Max :', max(self.liste))
        print('Min :', min(self.liste))
        print('Moyenne :', sum(self.liste)/len(self.liste))
if __name__ == "__main__":
    liste = input('Liste : ')
    obj = StatistiquesListe(liste)
    obj.afficher()
