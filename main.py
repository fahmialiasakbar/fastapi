from uuid import uuid4, UUID
from typing import List
from fastapi import FastAPI, HTTPException
from models import User, Gender, Role
app = FastAPI()

db: List[User] = [
    User(
        id=UUID("9e72bccb-6e65-4342-bfa9-f18046abfed8"),
        first_name="Fahmi",
        last_name="Akbar",
        gender=Gender.male,
        roles=[Role.student]
    ),
    User(
        id=UUID("c85f70b8-0516-48a0-805c-9f03ed9dba57"),
        first_name="Jack",
        last_name="Millder",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]

@app.get("/")
async def root():
    return {
        "Hello": "World"
    }

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {
        "id": user.id
    }

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return

    raise HTTPException(status_code = 404, detail=f"user with id:{user_id} does not exist")