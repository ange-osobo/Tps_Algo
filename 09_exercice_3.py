class ComptageOccurrences:
    def __init__(self, texte, mot):
        self.texte = texte
        self.mot = mot
    def compter(self):
        print(self.texte.count(self.mot))
if __name__ == "__main__":
    texte = input('Texte : ')
    mot = input('Mot : ')
    obj = ComptageOccurrences(texte, mot)
    obj.compter()
