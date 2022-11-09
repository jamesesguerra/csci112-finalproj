from pymongo import MongoClient


def attach_medical_records():
    for i in range(1, 1001):
        patient = patients.find({ "patient_id": i })
        patientObj = list(patient)[0]

        records = medical_records.find({ "patient_id": patientObj["patient_id"] })
        patientObj["medical_records"] = list(records)
        result = patients.replace_one({ "patient_id": i }, patientObj)
        print(result)


if __name__ == "__main__":
    try:
        cluster = MongoClient("mongodb+srv://mongo:mongo@csci112-cluster.zbudtoj.mongodb.net/HospitalAdministration?retryWrites=true&w=majority")
        db = cluster["HospitalAdministration"]
        print("Connected to MongoDB")
    except Exception as e:
        print("An error occurred...")
        print(e)

    patients = db["patients"]
    medical_records = db["medicalRecords"]

    attach_medical_records()