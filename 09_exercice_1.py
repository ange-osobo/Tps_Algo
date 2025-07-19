class NettoyerTexte:
    def __init__(self, texte):
        self.texte = texte
    def nettoyer(self):
        res = self.texte.strip().lower().replace('.', '!')
        print(res)
if __name__ == "__main__":
    texte = input('Texte : ')
    obj = NettoyerTexte(texte)
    obj.nettoyer()
