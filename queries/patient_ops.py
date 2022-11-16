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

    try:
        patients.insert_one(new_patient)
    except Exception as e:
        print(e)
    else:
        print(f"Patient {name} was successfully registered.")


# read
def get_patient_info(id=None, name=None):
    if id:
        patient = patients.find_one({ "patient_id": id })
    else:
        patient = patients.find_one({ "name": name })

    return patient


def get_patients_records(id=None, name=None):
    if id:
        medical_records = patients.find_one({ "patient_id": id })["medical_records"]
    else:
        medical_records = patients.find_one({ "name": name })["medical_records"]
    
    return medical_records


# update

# delete


if __name__ == "__main__":
    db = get_connection()
    patients = db["patients"]

    pprint(get_patients_records(name="Brigit Bes"))