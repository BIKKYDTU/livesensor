from pymongo import MongoClient
import pandas as pd

client = MongoClient("mongodb://localhost:27017/")
db = client["ineuron"]  # replace if different
collection = db["sensor"]  # replace if different

data = list(collection.find())
print(f"✅ Total documents found: {len(data)}")

if data:
    df = pd.DataFrame(data)
    print("✅ Columns:", df.columns.tolist())
    print("✅ Sample row:", df.head(1))
else:
    print("⚠️ No data found in collection.")
