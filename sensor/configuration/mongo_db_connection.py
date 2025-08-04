from dotenv import load_dotenv
import pymongo
from sensor.constant.database import DATABASE_NAME
import certifi
ca = certifi.where()
from sensor.constant.env_variable import MONGODB_URL_KEY
import os 
import logging 

from pathlib import Path

# 🔥 Force load .env from the root of the project
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)

class MongoDBClient:
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                print("🔥 MONGO_DB_URL_KEY =", MONGODB_URL_KEY)
                print("🔥 Loaded mongo_db_url =", mongo_db_url)
                logging.info(f"Retrieved MongoDB URL: {mongo_db_url}")

                if "localhost" in mongo_db_url:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url)
                else:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)   #TLS/SSl 
                
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            logging.error(f"Error initializing MongoDB client: {e}")
            raise
   
   