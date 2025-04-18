from config.database import user_collection
from config.database import medical_collection
from models.User import User
from models.medical import Medical

#insert data
user = User("vidhya","vidhya@gmail.com","Vidhya123")
result = user_collection.insert_one(user.to_dict())
id = result.inserted_id
name = user.username
medical = Medical(id, name, "common cold and fever")
medical_result = medical_collection.insert_one(medical.to_dict())
#fetch data
# for medical in medical_collection.find():
#     user_data = user_collection.find_one({"_id": medical["user_id"]})
#     print("Medical:", medical)
#     print("User:", user_data)

#delete data
medical_collection.delete_many({})
user_collection.delete_many({})
