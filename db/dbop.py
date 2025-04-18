from config.database import user_collection
from config.database import medical_collection
from models.User import User
from models.medical import Medical
from models.achievements import Achievement
#insert data
user = user_collection.find_one({"username": "vidhya"})
id = user.id
name = user.username
achievement = Achievement
#fetch data
for medical in medical_collection.find():
    user_data = user_collection.find_one({"_id": medical["user_id"]})
    print("Medical:", medical)
    print("User:", user_data)