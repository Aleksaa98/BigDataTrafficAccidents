from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["TrafficAccidentsDB"]
collection = db["Accidents"]

update_query = {
    "$set": {
        "VEH#": {"$toInt": "$VEH#"},
        "Trailers": {"$toInt": "$Trailers"},
        "INJ": {"$toInt": "$INJ"},
        "DEAD": {"$toInt": "$DEAD"},
        "DEER": {"$toInt": "$DEER"},
        "House#": {"$toInt": "$House#"},
        "Feet From": {"$toInt": "$Feet From"},
        "Latitude": {"$toDouble": "$Latitude"},
        "Longitude": {"$toDouble": "$Longitude"}
    }
}

collection.update_many({}, update_query)

print("Update completed successfully.")