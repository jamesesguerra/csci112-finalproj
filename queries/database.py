from pymongo import MongoClient


def get_connection():
    try:
        client = MongoClient("mongodb+srv://mongo:mongo@csci112-cluster.zbudtoj.mongodb.net/HospitalAdministration?retryWrites=true&w=majority")
        db = client["HospitalAdministration"]
        print("Connected to MongoDB")
        return db
    except Exception as e:
        print("An error occurred...")
        print(e)
