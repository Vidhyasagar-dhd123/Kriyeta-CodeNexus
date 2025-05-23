import pymongo
from pymongo import MongoClient

try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["Kriyeta"]
    user_collection = db["user"]
    medical_collection = db["medical"]
    achievement_collection = db["achievement"]
    chat_collection = db["chat"]
    print("Connected to the database successfully")
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
        medical_list = list(medical)
        if medical_list:
            return medical_list
        else:
            raise ValueError("Medical records not found")
    except Exception as e:
        print(f"Error fetching medical records: {e}")

def get_achievement_by_user_id(user_id):
    try:
        achievement = achievement_collection.find({"user_id": user_id})
        achievement_list = list(achievement)
        if achievement_list:
            return achievement_list
        else:
            raise ValueError("Achievements not found")
    except Exception as e:
        print(f"Error fetching achievements: {e}")

def get_chat_by_user_id(user_email):
    try:
        chat = chat_collection.find({"user_email": user_email})
        chat_list = list(chat)
        if chat_list:
            return chat_list
        else:
            raise ValueError("Chat records not found")
    except Exception as e:
        print(f"Error fetching chat records: {e}")
    # Handle the error appropriately here.
