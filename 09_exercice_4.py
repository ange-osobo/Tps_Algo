class GenerateurAcronyme:
    def __init__(self, phrase):
        self.phrase = phrase
    def generer(self):
        acr = ''.join(w[0].upper() for w in self.phrase.split())
        print('Acronyme :', acr)
if __name__ == "__main__":
    phrase = input('Phrase : ')
    obj = GenerateurAcronyme(phrase)
    obj.generer()
