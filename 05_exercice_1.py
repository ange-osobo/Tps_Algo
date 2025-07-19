class TableMultiplication:
    def __init__(self, nombre):
        self.nombre = nombre
    def generer(self):
        for i in range(1,13):
            print(f"{self.nombre} x {i} = {self.nombre * i}")
if __name__ == "__main__":
    nombre = int(input("Nombre : "))
    obj = TableMultiplication(nombre)
    obj.generer()
