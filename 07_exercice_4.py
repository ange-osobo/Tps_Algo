class FiltrerEtudiants:
    def __init__(self, etudiants):
        self.etudiants = etudiants
    def admis(self):
        admis = [n for n, note in self.etudiants if note >= 15]
        print('Étudiants admis :', admis)
if __name__ == "__main__":
    etudiants = input('Etudiants : ')
    obj = FiltrerEtudiants(etudiants)
    obj.admis()
