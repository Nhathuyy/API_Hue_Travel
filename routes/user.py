import collections
from tkinter import N
from fastapi import APIRouter
from models.user import User,Destination, Journey
from typing import List
from config.db import col
from fastapi import HTTPException
from schemas.user import UserEntity, userEntityResponse, UserCreate, UserUpdate
from bson.objectid import ObjectId
import json

app = APIRouter()

@app.get('/')
async def find_all_users():
    users_all = []
    all_users = col.find({})
    users = {}
    print(all_users)
    stt = -1
    for user_ne in all_users:
        stt += 1
        users[str(stt)] = str(user_ne)
    
    return users


@app.get("/users/{user_id}")
def get_user(user_id: str):
    # Tìm kiếm người dùng theo ID
    user = col.find_one({"_id": ObjectId(f"{user_id}")})

    if user is not None:
        return {
            "_id": str(user["_id"]),
            "name": user["name"],
            "age": user["age"],
            "email": user["email"],
            "numberofpp": user["numberofpp"],
            "amount": user["amount"],
            "interest": user["interest"],
            "ngay_di": user["ngay_di"],
            "ngay_den": user["ngay_den"]
        }
    else:
        return {"message": "User not found"}
    
@app.post('/')
async def create_user(user: User):
    col.insert_one(dict(user))
    return UserEntity(col.find())
@app.put('/{id}')
async def update_user(id: str, user: User):
    col.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
    return UserEntity(col.find_one({"_id": ObjectId(id)}))

@app.delete('/{id}')
async def delete_user(id: str):
    return UserEntity(col.find_one_and_delete({"_id": ObjectId(id)}))

users_db = []
destinations_db = []
journeys_db = []
# tao danh sach dia diem

# Destination routes
@app.get("/destinations", response_model=List[Destination])
def get_destinations():
    return destinations_db

@app.get("/destinations/{destination_id}", response_model=Destination)
def get_destination(destination_id: int):
    for destination in destinations_db:
        if destination.id == destination_id:
            return destination
    raise HTTPException(status_code=404, detail="Destination not found")
# Journey routes
@app.post("/generate-journey", response_model=Journey)
def generate_journey(user_id: int, destination_ids: List[int]):
    user = get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    destinations = [get_destination(dest_id) for dest_id in destination_ids]
    destinations = [dest for dest in destinations if dest is not None]

    if len(destinations) == 0:
        raise HTTPException(status_code=400, detail="No valid destinations selected")

    journey_id = len(journeys_db) + 1
    journey = Journey(id=journey_id, user_id=user_id, destination_ids=destination_ids)
    journeys_db.append(journey)
    return journey