import pymongo
from pymongo import MongoClient
from pprint import pprint


try:
    cluster = MongoClient("mongodb+srv://mongo:mongo@csci112-cluster.zbudtoj.mongodb.net/HospitalAdministration?retryWrites=true&w=majority")
    db = cluster["HospitalAdministration"]
    print("Connected to MongoDB")
except Exception as e:
    print(e)




