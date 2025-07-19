class GestionTemperature:
    def __init__(self, t):
        self.t = t
    def conseiller(self):
        if self.t >= 35: print("Très chaud, restez hydraté.")
        elif self.t >= 25: print("Chaud, faites attention au soleil.")
        elif self.t >= 15: print("Température agréable.")
        else: print("Il fait frais, couvrez-vous.")
if __name__ == "__main__":
    t = input("T : ")
    obj = GestionTemperature(t)
    obj.conseiller()
