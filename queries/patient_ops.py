from pymongo import MongoClient

from utils import get_max_id


def register_patient():
    pass


if __name__ == "__main__":
    try:
        cluster = MongoClient("mongodb+srv://mongo:mongo@csci112-cluster.zbudtoj.mongodb.net/HospitalAdministration?retryWrites=true&w=majority")
        db = cluster["HospitalAdministration"]
        print("Connected to MongoDB")
    except Exception as e:
        print("An error occurred...")
        print(e)

    patients = db["patients"]

    print(get_max_id(patients, "patient_id"))