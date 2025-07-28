# main.py
from model import UserModel
from view import UserView
from controller import UserController

if __name__ == "__main__":
    model = UserModel()
    view = UserView()
    controller = UserController(model, view)
    controller.run()
