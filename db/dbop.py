from config.database import user_collection
from config.database import medical_collection
from config.database import achievement_collection
from config.database import chat_collection
from models.chat import Chat
from models.User import User
from models.medical import Medical
from models.achievements import Achievement

# CRUD operations for User model
def create_user(user: User):
    return user_collection.insert_one(user.dict())

def read_user(user_id: str):
    return user_collection.find_one({"user_id": user_id})

def update_user(user_id: str, user_data: dict):
    return user_collection.update_one({"_id": user_id}, {"$set": user_data})

def delete_user(user_id: str):
    return user_collection.delete_one({"_id": user_id})

# CRUD operations for Medical model
def create_medical_record(medical: Medical):
    return medical_collection.insert_one(medical.dict())

def read_medical_record(user_id: str):
    return medical_collection.find_one({"_id": user_id})

def update_medical_record(user_id: str, medical_data: dict):
    return medical_collection.update_one({"_id": user_id}, {"$set": medical_data})

def delete_medical_record(user_id: str):
    return medical_collection.delete_one({"_id": user_id})
 
# CRUD operations for Achievement model
def create_achievement(achievement: Achievement):
    return achievement_collection.insert_one(achievement.dict())

def read_achievement(user_id: str):
    return achievement_collection.find_one({"_id": user_id})

def update_achievement(user_id: str, achievement_data: dict):
    return achievement_collection.update_one({"_id": user_id}, {"$set": achievement_data})

def delete_achievement(user_id: str):
    return achievement_collection.delete_one({"_id": user_id})

#CRUD operations for Chat model
def create_chat(chat: Chat):
    return chat_collection.insert_one(chat.dict())

def read_chat(user_email: str):
    return chat_collection.find_one({"user_email": user_email})

def update_chat(user_email: str, chat_data: dict):
    return chat_collection.update_one({"user_email": user_email}, {"$set": chat_data})

def delete_chat(user_email: str):
    return chat_collection.delete_one({"user_email": user_email})