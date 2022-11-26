from pymongo import MongoClient


def add_bill_dates():
    for i in range(1, 1003):
        record = medical_records.find_one({ "record_id": i })

        record_date = record["date"]
        bill_id = record["bill_id"]

        response = bills.update_one({ "bill_id": bill_id }, { "$set": { "date": record_date } })
        print(response)


if __name__ == "__main__":
    try:
        cluster = MongoClient("mongodb+srv://mongo:mongo@csci112-cluster.zbudtoj.mongodb.net/HospitalAdministration?retryWrites=true&w=majority")
        db = cluster["HospitalAdministration"]
        print("Connected to MongoDB")
    except Exception as e:
        print("An error occurred...")
        print(e)

    medical_records = db["medicalRecords"]
    bills = db["bills"]

    add_bill_dates()