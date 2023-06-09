# def userEntity(item) -> dict:
#     return{
#         "id": str(item["_id"]),
#         "name":item["name"],
#         "email":item["email"],
#         "password":item["password"]
#     }

# def userEntity(entity) -> list:
#     return [userEntity(item) for item in entity]


# class UserEntity(BaseModel):
#     name: str
#     email: str
#     password: str

# class userEntityResponse(UserEntity):
#     id: str
from typing import List, Optional

from pydantic import BaseModel, Field
from datetime import date
class UserEntity(BaseModel):
    name: str
    email: str

class userEntityResponse(UserEntity):
    id: str

class UserCreate(BaseModel):
    name: str
    email: str
    age: int
    numberofpp: int
    amount: str
    interest: str
    ngay_di: date
    ngay_den: date

class UserUpdate(BaseModel):
    name: str
    email: str
    age: int
    numberofpp: int
    amount: str
    interest: str
    ngay_di: date
    ngay_den: date

class User(UserCreate):
    id: str

    class Config:
        orm_mode = True



class Destination(BaseModel):
    id: int
    name: str
    location: str

class Journey(BaseModel):
    id: int
    user_id: int
    destination_ids: list[int]




