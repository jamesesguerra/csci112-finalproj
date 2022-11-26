from pymongo import MongoClient


def convert_to_array():
    medical_records.aggregate([
        {
            "$addFields": {
                "prescribed_drugs": { "$split": [ "$prescribed_drugs", "," ] }
            }
        },
        {
            "$out": "medicalRecords"
        }
    ])


if __name__ == "__main__":
    try:
        cluster = MongoClient("mongodb+srv://mongo:mongo@csci112-cluster.zbudtoj.mongodb.net/HospitalAdministration?retryWrites=true&w=majority")
        db = cluster["HospitalAdministration"]
        print("Connected to MongoDB")
    except Exception as e:
        print("An error occurred...")
        print(e)

    medical_records = db["medicalRecords"]

    convert_to_array()