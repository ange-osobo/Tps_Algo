class DiagnosticSante:
    def __init__(self, fievre):
        self.fievre = fievre
    def diagnostiquer(self):
        if self.fievre.lower() == 'oui':
            douleurs = input("Douleurs (oui/non) : ")
            print("Consulter un médecin" if douleurs.lower() == 'oui' else "Repos conseillé")
        else:
            tousse = input("Tousse (oui/non) : ")
            print("Repos conseillé" if tousse.lower() == 'oui' else "Bonne santé")
if __name__ == "__main__":
    fievre = input("Fievre : ")
    obj = DiagnosticSante(fievre)
    obj.diagnostiquer()
