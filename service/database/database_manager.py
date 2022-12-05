import pymongo

client = pymongo.MongoClient(
        "mongodb+srv://eagenlopamer:amer123@cluster0.62xfaj0.mongodb.net/?retryWrites=true&w=majority")
db = client.db_lasti

def get_user_collection() -> pymongo.collection :
        return db["users"]

def get_temperature_collection() -> pymongo.collection :
        return db["temperature"]

def get_feed_collection() -> pymongo.collection:
        return db["feeding"]

def get_tutor_information_collection() -> pymongo.collection:
        return db["tutor_info"]

def get_appointment_collection() -> pymongo.collection:
        return db["appointment"]