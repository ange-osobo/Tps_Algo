class ExtraireUnMotSurDeux:
    def __init__(self, phrase):
        self.phrase = phrase
    def extraire(self):
        m = self.phrase.split()
        print(m[::2])
if __name__ == "__main__":
    phrase = input('Phrase : ')
    obj = ExtraireUnMotSurDeux(phrase)
    obj.extraire()
