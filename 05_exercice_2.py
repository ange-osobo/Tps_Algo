class SommePairsListe:
    def __init__(self, nums):
        self.nums = nums
    def calculer(self):
        pairs = [x for x in self.nums if x % 2 == 0]
        print(f"Somme des pairs : {sum(pairs)}")
if __name__ == "__main__":
    nums = list(map(int, input('Entrez les valeurs séparées par espaces : ').split()))
    obj = SommePairsListe(nums)
    obj.calculer()
