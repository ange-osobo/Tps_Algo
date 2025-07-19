class CalculFactorielle:
    def __init__(self, n):
        self.n = n
    def calculer(self):
        fact = 1
        for i in range(1, self.n + 1):
            fact *= i
        print(f'Factorielle de {self.n} : {fact}')
if __name__ == "__main__":
    n = int(input('N : '))
    obj = CalculFactorielle(n)
    obj.calculer()
