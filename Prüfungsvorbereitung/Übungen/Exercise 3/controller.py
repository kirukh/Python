# controller.py
import model
from view import ask_name, show_name


class UserController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        name = self.view.ask_name()
        self.model.set_name(name)
        self.view.show_name(self.model.get_name())

    def fill_listbox(self):
        books = self.model.load_users()
        for book in books:
            print(
                f"Benutzer: {book['title']}, Alter: {book['author']}, Jahr: {book['year']}")
