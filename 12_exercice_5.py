class RapportTexte:
    def __init__(self, texte):
        self.texte = texte
    def generer(self):
        m = len(self.texte.split())
        c = len(self.texte)
        with open('rapport.txt','w') as f: f.write(f'Mots: {m}, Caractères: {c}\n')
if __name__ == "__main__":
    texte = input('Texte : ')
    obj = RapportTexte(texte)
    obj.generer()
