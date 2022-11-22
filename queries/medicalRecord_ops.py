from pprint import pprint
from datetime import datetime

from database import get_connection
from utils import get_max_id
from bill_ops import create_bill


# create
def add_record(patient_id, doctor_id, room_id, prescribed_drugs, bill_amount):
    bill_id = create_bill(bill_amount)

    new_record = {
        "record_id": get_max_id(medical_records, "record_id") + 1,
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "room_id": room_id,
        "bill_id": bill_id,
        "date": datetime.now().strftime("%m/%d/%Y"),
        "prescribed_drugs": prescribed_drugs
    }

    medical_records.insert_one(new_record)
    patients.update_one({ "patient_id": patient_id }, { "$push": { "medical_records": new_record } })
    print(f"Medical record for patient #{patient_id} successfully added.")


# read
def get_record_info(id):
    record = medical_records.find_one({ "record_id": id })
    return record


# update
def update_record_info(id, attribute, value):
    medical_records.update_one({ "record_id": id }, { "$set": { attribute: value } })

    print("Medical record successfully updated.")


# delete
def remove_record(id):
    medical_records.delete_one({ "record_id": id })

    print("Medical record successfully deleted.")


if __name__ == "__main__":
    db = get_connection()
    medical_records = db["medicalRecords"]
    bills = db["bills"]
    patients = db["patients"]


    