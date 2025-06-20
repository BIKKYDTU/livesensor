from dataclasses import dataclass
import os
import pymongo

@dataclass
class EnvironmentVariable:
    mongo_db_url: str = os.getenv("MONGO_DB_URL")

# Instantiate after class definition
env_var = EnvironmentVariable()

# Create MongoDB client using the environment variable
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
