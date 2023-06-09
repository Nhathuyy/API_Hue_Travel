# from pydantic import BaseModel

# class User(BaseModel):
#     name: str
#     email: str
#     password: str

# from pydantic import BaseModel
from datetime import date
# from enum import Enum


# class Interest(str, Enum):
#     cultural_heritage = "di_san_van_hoa"
#     natural_heritage = "di_san_thien_nhien"
#     entertainment = "vui_choi_giai_tri"


# class User(BaseModel):
#     name: str
#     age: int
#     email: str
#     password: str
#     numberofpp: int
#     amount: float
#     interest: Interest
#     start_date: date
#     end_date: date
from pydantic import BaseModel, Field
from bson import ObjectId
from typing import List, Optional

class User(BaseModel):
    name: str
    age: int
    email: str
    numberofpp: int
    amount: str
    interest: str
    ngay_di: date
    ngay_den: date


class Destination(BaseModel):
    id: int
    name: str
    location: str

class Journey(BaseModel):
    id: int
    user_id: int
    destination_ids: list[int]