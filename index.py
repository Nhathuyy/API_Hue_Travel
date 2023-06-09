import collections
from fastapi import FastAPI, APIRouter, HTTPException, status
from models.user import User,Destination, Journey
from config.db import col
from bson.objectid import ObjectId
import json
from datetime import date
from schemas.user import UserEntity, userEntityResponse, UserCreate, UserUpdate
from typing import List

app = FastAPI()
router = APIRouter()



@router.post("/users/insert-user")
def create_user(user: User):
    try:
        # Chuyển đổi đối tượng User thành đối tượng dict
        user_dict = user.dict()

        # Chuyển đổi giá trị ngày thành chuỗi
        user_dict["ngay_di"] = str(user_dict["ngay_di"])
        user_dict["ngay_den"] = str(user_dict["ngay_den"])

        # Thêm tài liệu vào cơ sở dữ liệu
        result = col.insert_one(user_dict)
        user_id = result.inserted_id
        # user_id = result.inserted_id
        print("result ", str(result))
        user = col.find_one({"_id": ObjectId(f"{user_id}")})
#   
        if result is None:
            return {
                "code": 403,
                "status": "failed",
                "message": "Cannot create user",
                
            }
        return {
            "code": 201,
            "status": "success",
            "message": "Create user is successfully",
            "_id": str(user["_id"])
            # "data": {
            #         "user_id": str(user_id)
            #     }
        }
    except Exception as e:
        return {
            "code": 500,
            "status": "failed",
            "message": "An error occurred",
            "error": str(e),
        }
@router.get("/users/{user_id}")
def get_user(user_id: str):
    try:
        # Tìm kiếm người dùng theo ID
        user = col.find_one({"_id": ObjectId(user_id)})

        if user:
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
    except Exception as e:
        return {"message": "An error occurred", "error": str(e)}

# @router.post("/users/insert-user")
# def create_user(user: User):
#     # Chuyển đổi đối tượng User thành đối tượng dict
#     user_dict = user.dict()
#     print(type(user_dict))
#     # Thêm tài liệu vào cơ sở dữ liệu
#     result = col.insert_one(user_dict)
#     user_id = result.inserted_id
#     # Trả về thông tin tài liệu vừa được tạo
#     # created_user = {
#     #     "_id": ObjectId(result.inserted_id)
#     #     **user_dict
#     # }
#     user = col.find_one({"_id": ObjectId(f"{user_id}")})
#     if user is not None:
#         return {
#             "_id": str(user["_id"]),
#             "name": user["name"],
#             "age": user["age"],
#             "email": user["email"],
#             "numberofpp": user["numberofpp"],
#             "amount": user["amount"],
#             "interest": user["interest"],
#             "ngay_di": user["ngay_di"],
#             "ngay_den": user["ngay_den"]
#         }
#     else:
#         return {"message": "User not found"}
        
#     return created_user
# @router.get("/users/{user_id}")
# def get_user(user_id: str):
#     # Tìm kiếm người dùng theo ID
#     user = col.find_one({"_id": ObjectId(user_id)})

#     if user:
#         return {
#             "_id": str(user["_id"]),
#             "name": user["name"],
#             "email": user["email"],
#             "password": user["password"]
#         }
#     else:
#         return {"message": "User not found"}


# @router.get("/users/{user_id}")
# def read_user(user_id: str):
#     # Tìm kiếm tài liệu theo ID
#     user = col.find_one({"_id": ObjectId(user_id)})

#     if user:
#         return user
#     else:
#         return {"message": "User not found"}


@router.put("/users/{user_id}")
def update_user(user_id: str, user: User):
    # Chuyển đổi đối tượng User thành đối tượng dict
    user_dict = user.dict()

    # Cập nhật tài liệu trong cơ sở dữ liệu
    result = col.update_one({"_id": ObjectId(user_id)}, {"$set": user_dict})

    if result.modified_count == 1:
        updated_user = {
            "id": user_id,
            **user_dict
        }
        return updated_user
    else:
        return {"message": "User not found"}


@router.delete("/users/{user_id}")
def delete_user(user_id: str):
    # Xóa tài liệu theo ID
    result = col.delete_one({"_id": ObjectId(user_id)})

    if result.deleted_count == 1:
        return {"message": "User deleted successfully"}
    else:
        return {"message": "User not found"}


@router.get("/users")
def get_all_users():
    # Lấy danh sách tất cả các user
    users = col.find({}, {"_id": 1})

    # Chuyển đổi ObjectId thành str và lưu vào list
    user_ids = [str(user["_id"]) for user in users]

    return user_ids

destinations_db = []
# Route xử lý lấy danh sách địa điểm
@router.get("/destinations", response_model=List[Destination])
def get_destinations():
    return destinations_db

# Route xử lý lấy thông tin địa điểm theo ID
@router.get("/destinations/{destination_id}", response_model=Destination)
def get_destination(destination_id: int):
    for destination in destinations_db:
        if destination.id == destination_id:
            return destination
    raise HTTPException(status_code=404, detail="Destination not found")
journeys_db=[]
# Route xử lý tạo hành trình mới
@router.post("/generate-journey", response_model=Journey)
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

app.include_router(router)
