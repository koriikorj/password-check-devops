# password_checker.py
def is_valid_password(password):
    """
    Gültiges Passwort erfüllt:
    - mind. 8 Zeichen
    - enthält Zahl
    - enthält Groß- und Kleinbuchstaben
    """
    if len(password) < 8:
        return False
    if not any(c.isdigit() for c in password): #nur ziffern
        return False
    if not any(c.islower() for c in password): #nur kleine Buchstaben
        return False
    if not any(c.isupper() for c in password): #nur große Buchstaben
        return False
    return True

pas = input()
if is_valid_password(pas):
    print("Passwort ist gültig")
else:
    print("Passwort ist ungültig")
