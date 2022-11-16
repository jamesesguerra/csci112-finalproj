def get_max_id(collection, field_name):
    result = collection.aggregate([
        {
            "$group": { "_id": 0, "max_id": { "$max": f"${field_name}" } }
        }
    ])

    return list(result)[0]["max_id"]