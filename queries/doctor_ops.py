from pprint import pprint

from database import get_connection
from utils import get_max_id


# create
def add_doctor(name, gender, age, contact_number, specialization):
    new_doctor = {
        "doctor_id": get_max_id(doctors, "doctor_id") + 1,
        "name": name,
        "gender": gender,
        "age": age,
        "contact_number": contact_number,
        "specialization": specialization
    }

    doctors.insert_one(new_doctor)


# read
def get_doctor_info(id=None, name=None):
    if id:
        doctor = doctors.find_one({ "doctor_id": id })
    else:
        doctor = doctors.find_one({ "name": name })

    return doctor


# update
def update_doctor_info(attribute, value, id=None, name=None):
    if id:
        doctors.update_one({ "doctor_id": id }, { "$set": { attribute: value } })
    else:
        doctors.update_one({ "name": name }, { "$set": { attribute: value } })


# delete
def remove_doctor(id=None, name=None):
    if id:
        doctors.delete_one({ "doctor_id": id })
    else:
        doctors.delete_one({ "name": name })
        
    
if __name__ == "__main__":
    db = get_connection()
    doctors = db["doctors"]
    