class DivisionProtegee:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def diviser(self):
        try:
            print(self.a / self.b)
        except ZeroDivisionError:
            print('Erreur : division par zéro')
if __name__ == "__main__":
    a = int(input('A : '))
    b = int(input('B : '))
    obj = DivisionProtegee(a, b)
    obj.diviser()
