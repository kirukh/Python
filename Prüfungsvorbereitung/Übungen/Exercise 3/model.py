import json


class UserModel:
    def __init__(self, json_path="books.json"):
        self.json_path = json_path
        self.users = []

    def load_users(self):
        with open(self.json_path, 'r') as file:
            data = json.load(file)
            return data

    def get_users(self):
        return self.users
