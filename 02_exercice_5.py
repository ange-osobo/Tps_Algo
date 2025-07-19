class ConvertisseurDevises:
    def __init__(self, usd):
        self.usd = usd
    def convertir(self):
        print(f"EUR : {self.usd * 0.93:.2f}")
        print(f"CFA : {self.usd * 610:.2f}")
        print(f"GBP : {self.usd * 0.79:.2f}")
if __name__ == "__main__":
    usd = float(input("Usd : "))
    obj = ConvertisseurDevises(usd)
    obj.convertir()
