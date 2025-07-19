class ComptageVoyelles:
    def __init__(self, mots):
        self.mots = mots
    def compter(self):
        vowels = set('aeiouyAEIOUY')
        count = sum(c in vowels for w in self.mots for c in w)
        print(f"Nombre de voyelles : {count}")
if __name__ == "__main__":
    mots = input('Entrez les mots séparés par espaces : ').split()
    obj = ComptageVoyelles(mots)
    obj.compter()
