class CalculateurAvantages:
    def __init__(self, anciennete, performance):
        self.anciennete = anciennete
        self.performance = performance
    def calculer_prime(self):
        if self.anciennete >= 5:
            prime = 2000 if self.performance >= 4 else 1000
        else:
            prime = 500 if self.performance >= 4 else 0
        print(f"Prime : {prime} €")
if __name__ == "__main__":
    anciennete = int(input("Anciennete : "))
    performance = int(input("Performance : "))
    obj = CalculateurAvantages(anciennete, performance)
    obj.calculer_prime()
