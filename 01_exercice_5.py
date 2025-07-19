class Vitesse:
    def __init__(self, distance, temps):
        self.distance = distance
        self.temps = temps

    def calculer_vitesse(self):
        v_kmh = self.distance / self.temps
        v_ms = v_kmh * 1000 / 3600
        print(f"Vitesse moyenne : {v_kmh:.2f} km/h, soit {v_ms:.2f} m/s")
if __name__ == "__main__":
    d = float(input("Distance (km) : "))
    t = float(input("Temps (h) : "))
    v = Vitesse(d, t)
    v.calculer_vitesse()
