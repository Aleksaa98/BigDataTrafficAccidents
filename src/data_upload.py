import csv
from urllib.parse import quote_plus
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# password = quote_plus('Welikialeksa1234')
#uri = "mongodb+srv://popovaleksa321:" + password + "@cluster0.2r9ydlh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
uri = "mongodb://localhost:27017"

client = MongoClient(uri)  #server_api=ServerApi('1')
db = client["TrafficAccidentsDB"]
collection = db["Accidents"]

# Path to CSV
csv_path = "../data/traffic_accidents.csv"

# Read and upload data
with open(csv_path, "r") as file:
    csv_reader = csv.DictReader(file)
    data = list(csv_reader)
    collection.insert_many(data)