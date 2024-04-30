import csv
from pymongo import MongoClient

# password = quote_plus('Password')
#uri = "mongodb+srv://popovaleksa321:" + password + "@cluster0.2r9ydlh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


# Upload data function
def upload_data():
    uri = "mongodb://localhost:27017"
    client = MongoClient(uri)  # server_api=ServerApi('1')
    db = client["TrafficAccidentsDB"]
    collection = db["Accidents"]

    csv_path = "../data/traffic_accidents.csv"
    with open(csv_path, "r") as file:
        csv_reader = csv.DictReader(file)
        data = list(csv_reader)
        collection.insert_many(data)


if __name__ == "__main__":
    upload_data()