from pymongo import MongoClient


try:
    cluster = MongoClient("mongodb+srv://mongo:mongo@csci112-cluster.zbudtoj.mongodb.net/HospitalAdministration?retryWrites=true&w=majority")
    db = cluster["HospitalAdministration"]
    print("Connected to MongoDB")
except Exception as e:
    print("An error occurred...")
    print(e)




