class ExtraireMilieu:
    def __init__(self, mot):
        self.mot = mot
    def extraire(self):
        print(self.mot[2:-2])
if __name__ == "__main__":
    mot = input('Mot : ')
    obj = ExtraireMilieu(mot)
    obj.extraire()
