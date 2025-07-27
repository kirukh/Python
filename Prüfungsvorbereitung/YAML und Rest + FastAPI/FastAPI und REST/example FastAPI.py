# Datei: main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Datenmodell


class User(BaseModel):
    id: int
    name: str
    email: str


# Fake-Datenbank
users = []

# GET - Alle Benutzer anzeigen


@app.get("/users")
def get_users():
    return users


# POST - Benutzer hinzufügen
@app.post("/users")
def create_user(user: User):
    users.append(user)
    return {"message": "User added"}

# GET - Einzelnen Benutzer abrufen


@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    return {"error": "User not found"}
