from pymongo import MongoClient

from utils import get_max_id


def register_patient(name, gender, age, height, weight, contact_number):
    new_patient = {
        "patient_id": get_max_id(patients, "patient_id") + 1,
        "name": name,
        "gender": gender,
        "age": age,
        "height": height,
        "weight": weight,
        "contact_number": contact_number,
        "medical_records": []
    }

    try:
        patients.insert_one(new_patient)
    except Exception as e:
        print(e)
    else:
        print(f"Patient {name} was successfully registered.")


if __name__ == "__main__":
    try:
        cluster = MongoClient("mongodb+srv://mongo:mongo@csci112-cluster.zbudtoj.mongodb.net/HospitalAdministration?retryWrites=true&w=majority")
        db = cluster["HospitalAdministration"]
        print("Connected to MongoDB")
    except Exception as e:
        print("An error occurred...")
        print(e)

    patients = db["patients"]

    register_patient("John dela Cruz", "Male", 45, 178, 90.5, "383-228-238")