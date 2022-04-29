from uuid import uuid4
from typing import List
from fastapi import FastAPI
from models import User, Gender, Role
app = FastAPI()

db: List[User] = [
    User(
        id = uuid4(),
        fist_name = "Fahmi",
        last_name = "Fakbar",
        gender = Gender.male,
        roles = [Role.student]
    ),
    User(
        id = uuid4(),
        first_name = "Jack",
        last_name = "Millder",
        gender = Gender.male,
        roles = [Role.admin, Role.user]
    )
]

@app.get("/")
async def root():
    return {
        "Hello" : "World"
    }


