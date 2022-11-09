import pymongo
from pymongo import MongoClient
from pprint import pprint


try:
    cluster = MongoClient("mongodb+srv://mongo:mongo@csci112-cluster.zbudtoj.mongodb.net/HospitalAdministration?retryWrites=true&w=majority")
    db = cluster["HospitalAdministration"]
    print("Connected to MongoDB")
    patients = db["patients"]
    medical_records = db["medicalRecords"]
except Exception as e:
    print(e)


def attach_medical_records():
    for i in range(1, 1001):
        patient = patients.find({ "patient_id": i })
        patientObj = list(patient)[0]

        records = medical_records.find({ "patient_id": patientObj["patient_id"] })
        patientObj["medical_records"] = list(records)
        result = patients.replace_one({ "patient_id": i }, patientObj)
        print(result)

attach_medical_records()