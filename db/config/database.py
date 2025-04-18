import pymongo
from pymongo import MongoClient

try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["Kriyeta"]
    user_collection = db["user"]
    medical_collection = db["medical"]
except pymongo.errors.ConnectionFailure as e:
    print("Failed to connect to the database:", e)


def get_user_by_id(user_id):
    try:
        user = user_collection.find_one({"_id": user_id})
        if user:
            return user
        else:
            raise ValueError("User not found")
    except Exception as e:
        print(f"Error fetching user: {e}")
        # Handle the error appropriately here.
def get_medical_by_user_id(user_id):
    try:
        medical = medical_collection.find({"user_id": user_id})
        if medical:
            return medical
        else:
            raise ValueError("Medical records not found")
    except Exception as e:
        print(f"Error fetching medical records: {e}")
    # Handle the error appropriately here.
