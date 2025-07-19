class ClassificationNotes:
    def __init__(self, note):
        self.note = note
    def classer(self):
        mention = ""
        if self.note >= 90: mention = "Excellent"
        elif self.note >= 75: mention = "Très Bien"
        elif self.note >= 60: mention = "Bien"
        elif self.note >= 50: mention = "Passable"
        else: mention = "Insuffisant"
        print(f"Mention : {mention}")
if __name__ == "__main__":
    note = input("Note : ")
    obj = ClassificationNotes(note)
    obj.classer()
