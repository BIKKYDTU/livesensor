from pymongo import MongoClient

# ✅ Directly use your correct MongoDB Atlas URI
MONGO_URI = "mongodb+srv://BIKKY8586:BIKKY8586@cluster0.nu7og55.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)

# ✅ Use your actual DB and collection names
db = client["sensor_db"]
collection = db["training_data"]

# ❗ Delete all documents from the collection
result = collection.delete_many({})
print(f"Deleted {result.deleted_count} documents.")




from sensor.exception import SensorException
import os 
import sys

from sensor.logger import logging
from sensor.utils2 import dump_csv_file_to_mongodb_collection
#def test_exception():
 #   try:
 #       logging.info("ki yaha p bhaiaa ek error ayegi diveision by zero wali error ")
 #       a=1/0
 #   except Exception as e:
 #      raise SensorException(e,sys) 
      




if __name__ == "__main__":
    file_path = r"C:\Users\ASUS\Desktop\SENSORLIVE\aps_failure_training_set1.csv"
    database_name = "sensor_db"
    collection_name = "training_data"
    dump_csv_file_to_mongodb_collection(file_path, database_name, collection_name)
            