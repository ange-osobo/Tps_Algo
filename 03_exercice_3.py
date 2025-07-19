class CalculFraisLivraison:
    def __init__(self, val):
        self.val = val
    def calculer(self):
        if self.val >= 100: frais = 0
        elif self.val >= 50: frais = 5
        else: frais = 10
        print(f"Total à payer : {self.val + frais:.2f} €")
if __name__ == "__main__":
    val = input("Val : ")
    obj = CalculFraisLivraison(val)
    obj.calculer()
