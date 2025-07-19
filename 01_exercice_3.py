class ConvertisseurDuree:
    def __init__(self, heures, minutes, secondes):
        self.heures = heures
        self.minutes = minutes
        self.secondes = secondes

    def total_secondes(self):
        total = self.heures * 3600 + self.minutes * 60 + self.secondes
        print(f"Durée totale en secondes : {total}")
if __name__ == "__main__":
    h = int(input("Heures : "))
    m = int(input("Minutes : "))
    s = int(input("Secondes : "))
    c = ConvertisseurDuree(h, m, s)
    c.total_secondes()
