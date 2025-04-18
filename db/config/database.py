import pymongo

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["Kriyeta"]
user_collection = db["user"]
medical_collection = db["medical"]