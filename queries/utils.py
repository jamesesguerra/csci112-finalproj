def get_max_id(collection, field_name):
    """
    A function that takes in a collection in MongoDB and the field name of the 
    id, and returns the maximum id number in that collection (just so we can mock
    an auto increment id when we add new documents)
    """
    result = collection.aggregate([
        {
            "$group": { "_id": 0, "max_id": { "$max": f"${field_name}" } }
        }
    ])

    return list(result)[0]["max_id"]