from pymongo import MongoClient
from pprint import pprint

from database import get_connection
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


def get_patient_info(id=None, name=None):
    if id:
        patient = patients.find({ "patient_id": id })
        return list(patient)
    else:
        patient = patients.find({ "name": name })
        return list(patient)


if __name__ == "__main__":
    db = get_connection()
    patients = db["patients"]

    pprint(get_patient_info(name="Brigit Bes"))