# view.py
class UserView:
    def show_name(self, name):
        print(f"Der Name des Benutzers ist: {name}")

    def ask_name(self):
        return input("Bitte gib deinen Namen ein: ")
