# CSCI 112 Final Project

## Development Environment Setup

Clone the repository
```sh
# ssh
git clone git@github.com:jamesesguerra/csci112-finalproj.git

# or

# https
git clone https://github.com/jamesesguerra/csci112-finalproj.git
```

Change directory into folder
```sh
cd csci112-finalproj
```

Make a virtual environment
```sh
python -m venv venv
```

Activate the environment
```sh
# windows
\venv\Scripts\activate

# unix
source venv/bin/activate
```

Install project dependencies
```sh
pip install -r requirements.txt
```

## Database Usage

1. To use the database associated with the project, add "HospitalAdministration" as a path parameter in the MongoDB URI used to connect to the MongoDB Atlas cluster:
```sh
mongodb+srv://mongo:mongo@csci112-cluster.zbudtoj.mongodb.net/HospitalAdministration?retryWrites=true&w=majority
```

2. Import the `MongoClient` class from the pymongo package. The MongoDB URI must then be passed to it when creating an instance of the client:
```py
from pymongo import MongoClient

client = MongoClient("mongodb+srv://mongo:mongo@csci112-cluster.zbudtoj.mongodb.net/HospitalAdministration?retryWrites=true&w=majority")
```

3. Access the `HospitalAdministration` database from the client object:
```py
db = client["HospitalAdministration"]
```

## Data Model of the Database
![image](https://user-images.githubusercontent.com/68677613/204084506-c5c0c3d0-88ed-41bf-bbe2-eb38c9886eeb.png)

