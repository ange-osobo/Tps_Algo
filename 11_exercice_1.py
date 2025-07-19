class Calculatrice:
    def __init__(self, a, b, op):
        self.a = a
        self.b = b
        self.op = op
    def calculer(self):
        ops = {'+': self.a + self.b, '-': self.a - self.b, '*': self.a * self.b, '/': self.a / self.b}
        print(ops.get(self.op, 'Opération invalide'))
if __name__ == "__main__":
    a = int(input('A : '))
    b = int(input('B : '))
    op = input('Op : ')
    obj = Calculatrice(a, b, op)
    obj.calculer()
