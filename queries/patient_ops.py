from pprint import pprint

from database import get_connection
from utils import get_max_id


# create
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

    patients.insert_one(new_patient)


# read
def get_patient_info(id=None, name=None):
    if id:
        patient = patients.find_one({ "patient_id": id }, { "medical_records": 0 })
    else:
        patient = patients.find_one({ "name": name }, { "medical_records": 0 })

    return patient


def get_patients_records(id=None, name=None):
    if id:
        medical_records = patients.find_one({ "patient_id": id })["medical_records"]
    else:
        medical_records = patients.find_one({ "name": name })["medical_records"]
    
    return medical_records


def get_assigned_doctors(id=None, name=None):
    key = "patient_id" if id else "name"
    doctors = patients.aggregate([
        {
            "$match": { key: id if id else name }
        },
        {
            "$unwind": "$medical_records"
        },
        {
            "$group": {
                "_id": "$medical_records.doctor_id",
                "times_assigned": { "$sum": 1 }
            }
        },
        {
            "$sort": { "times_assigned": -1 }
        },
        {
            "$project": { "_id": 0, "doctor_id": "$_id", "times_assigned": 1 }
        }
    ])
    return list(doctors)


def get_avg_patient_age():
    avg_age = patients.aggregate([
        {
            "$group": { "_id": 1, "avg_age": { "$avg": "$age" } }
        }
    ])
    return list(avg_age)[0]["avg_age"]


# update
def update_patient_info(attribute, value, id=None, name=None):
    if id:
        patients.update_one({ "patient_id": id }, { "$set": { attribute: value } })
    else:
        patients.update_one({ "name": name }, { "$set": { attribute: value } })


# delete
def remove_patient(id=None, name=None):
    if id:
        patients.delete_one({ "patient_id": id })
    else:
        patients.delete_one({ "name": name })


if __name__ == "__main__":
    db = get_connection()
    patients = db["patients"]


    pprint(get_avg_patient_age())