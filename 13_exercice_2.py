class ConversionSecurisee:
    def __init__(self, texte):
        self.texte = texte
    def convertir(self):
        try:
            print(int(self.texte))
        except ValueError:
            print('Erreur : conversion impossible')
if __name__ == "__main__":
    texte = input('Texte : ')
    obj = ConversionSecurisee(texte)
    obj.convertir()
