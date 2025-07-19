class VerifDivisible:
    def __init__(self, n):
        self.n = n
    def verifier(self):
        if self.n % 3 == 0 and self.n % 5 == 0:
            print("Divisible par 3 et 5")
        else:
            print("Pas divisible par 3 et 5")
if __name__ == "__main__":
    n = input("N : ")
    obj = VerifDivisible(n)
    obj.verifier()
