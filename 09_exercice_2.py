class ValidationEmail:
    def __init__(self, email):
        self.email = email
    def valider(self):
        print('Valide' if self.email.endswith('@gmail.com') else 'Invalide')
if __name__ == "__main__":
    email = input('Email : ')
    obj = ValidationEmail(email)
    obj.valider()
