class NoteSur100:
    def __init__(self, note20):
        self.note20 = note20

    def note100(self):
        result = (self.note20 / 20) * 100
        print(f"Note sur 100 : {result:.2f}")
if __name__ == "__main__":
    note20 = float(input("Note sur 20 : "))
    note = NoteSur100(note20)
    note.note100()
