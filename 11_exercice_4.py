class ConvertisseurMultiDevises:
    def __init__(self, usd):
        self.usd = usd
    def convertir(self):
        print(self.usd*0.93, self.usd*610, self.usd*0.79)
if __name__ == "__main__":
    usd = input('Usd : ')
    obj = ConvertisseurMultiDevises(usd)
    obj.convertir()
