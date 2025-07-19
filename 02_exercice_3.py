class CalculateurFacture:
    def __init__(self, ht, tva):
        self.ht = ht
        self.tva = tva
    def calculer_ttc(self):
        ttc = self.ht * (1 + self.tva / 100)
        print(f"Montant TTC : {ttc:.2f} €")
if __name__ == "__main__":
    ht = float(input("Ht : "))
    tva = float(input("Tva : "))
    obj = CalculateurFacture(ht, tva)
    obj.calculer_ttc()
