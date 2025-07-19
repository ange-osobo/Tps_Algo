class SauvegardeUsers:
    def __init__(self, users):
        self.users = users
    def sauvegarder(self):
        with open('users.txt', 'w') as f: f.write('\n'.join(self.users))
if __name__ == "__main__":
    users = input('Utilisateurs séparés par virgules : ').split(',')
    obj = SauvegardeUsers(users)
    obj.sauvegarder()
