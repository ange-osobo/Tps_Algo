class JournalActivites:
    def __init__(self, activite):
        self.activite = activite
    def ajouter(self):
        with open('journal.txt', 'a') as f: f.write(self.activite + '\n')
if __name__ == "__main__":
    activite = input('Activite : ')
    obj = JournalActivites(activite)
    obj.ajouter()
