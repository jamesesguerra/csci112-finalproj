#!/bin/bash

# script to import datasets to DB

mongoimport --uri "mongodb+srv://mongo:mongo@csci112-cluster.zbudtoj.mongodb.net/HospitalAdministration?retryWrites=true&w=majority" -d HospitalAdministration -c patients --type csv --file patients.csv --headerline

mongoimport --uri "mongodb+srv://mongo:mongo@csci112-cluster.zbudtoj.mongodb.net/HospitalAdministration?retryWrites=true&w=majority" -d HospitalAdministration -c doctors --type csv --file doctors.csv --headerline

mongoimport --uri "mongodb+srv://mongo:mongo@csci112-cluster.zbudtoj.mongodb.net/HospitalAdministration?retryWrites=true&w=majority" -d HospitalAdministration -c bills --type csv --file bills.csv --headerline

mongoimport --uri "mongodb+srv://mongo:mongo@csci112-cluster.zbudtoj.mongodb.net/HospitalAdministration?retryWrites=true&w=majority" -d HospitalAdministration -c rooms --type csv --file rooms.csv --headerline

mongoimport --uri "mongodb+srv://mongo:mongo@csci112-cluster.zbudtoj.mongodb.net/HospitalAdministration?retryWrites=true&w=majority" -d HospitalAdministration -c medicalRecords --type csv --file medicalRecords.csv --headerline
