from ipaddress import collapse_addresses
from pymongo import MongoClient

# Kết nối tới MongoDB
client = MongoClient("mongodb+srv://huetravel:nhathuy2001@cluster0.xwhsaa4.mongodb.net/?retryWrites=true&w=majority")
# Chọn cơ sở dữ liệu
db = client["huetravel_web"]


# # collection_name = db["todos_app"]
# # Chọn bộ sưu tập người dùng
col = db["users"]
# users_collection = db["users"]
# destinations_collection = db["destinations"]