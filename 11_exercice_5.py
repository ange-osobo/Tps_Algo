class GenerateurMotDePasse:
    def __init__(self, n):
        self.n = n
    def generer(self):
        import random, string
        pw = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(self.n))
        print(pw)
if __name__ == "__main__":
    n = int(input('N : '))
    obj = GenerateurMotDePasse(n)
    obj.generer()
