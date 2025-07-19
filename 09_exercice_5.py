class MasquerMot:
    def __init__(self, phrase, mot):
        self.phrase = phrase
        self.mot = mot
    def masquer(self):
        res = self.phrase.replace(self.mot, '*'*len(self.mot))
        print(res)
if __name__ == "__main__":
    phrase = input('Phrase : ')
    mot = input('Mot : ')
    obj = MasquerMot(phrase, mot)
    obj.masquer()
