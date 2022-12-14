from pprint import pprint
from random import randint

from database import get_connection
from utils import get_max_id


# create
def create_bill(amount):
    db = get_connection()
    bills = db["bills"]
    invoice_number = ''.join(["{}".format(randint(0, 9)) for _ in range(0, 10)])
    bill_id = get_max_id(bills, "bill_id") + 1

    new_bill = {
        "bill_id": bill_id,
        "amount": amount,
        "invoice_number": invoice_number
    }

    bills.insert_one(new_bill)
    return bill_id


# read
def get_bill_info(id):
    bill = bills.find_one({ "bill_id": id })
    return bill


def get_total_amount(date):
    total = bills.aggregate([
        {
            "$match": { "date": date }
        },
        {
            "$group": { "_id": 1, "total_amount": { "$sum": "$amount" } }
        }
    ])
    return list(total)[0]["total_amount"]


# update
def update_bill_info(id, attribute, value):
    bills.update_one({ "bill_id": id }, { "$set": { attribute: value } })


# delete
def remove_bill(id):
    bills.delete_one({ "bill_id": id })

    
if __name__ == "__main__":
    db = get_connection()
    bills = db["bills"]

    pprint(get_total_amount("01/03/2022"))
