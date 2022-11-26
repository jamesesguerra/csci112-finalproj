from pprint import pprint

from database import get_connection
from utils import get_max_id


# create
def add_room(room_type):
    new_room = {
        "room_id": get_max_id(rooms, "room_id") + 1,
        "room_type": room_type
    }

    rooms.insert_one(new_room)

    
# read
def get_room_info(id):
    room = rooms.find_one({ "room_id": id })
    return room


# update
def update_room_info(id, attribute, value):
    rooms.update_one({ "room_id": id }, { "$set": { attribute: value } })


# delete
def remove_room(id):
    rooms.delete_one({ "room_id": id })


if __name__ == "__main__":
    db = get_connection()
    rooms = db["rooms"]

    