from pprint import pprint

from database import get_connection
from utils import get_max_id


if __name__ == "__main__":
    db = get_connection()
    medical_records = db["medicalRecords"]


    