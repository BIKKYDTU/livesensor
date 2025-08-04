from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["sensor_db"]  # make sure this matches
collection = db["sensor_data"]  # make sure this matches

print("✅ Total documents:", collection.count_documents({}))
print("🔍 Sample document:\n", collection.find_one())
