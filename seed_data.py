from sensor.utils2 import dump_csv_file_to_mongodb_collection

file_path = r"C:\Users\ASUS\Desktop\SENSORLIVE\aps_failure_training_set1.csv"
DATABASE_NAME = "ineuron"
COLLECTION_NAME = "sensor"

dump_csv_file_to_mongodb_collection(file_path, DATABASE_NAME, COLLECTION_NAME)
print("✅ Data inserted into MongoDB.")
