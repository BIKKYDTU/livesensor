import sys
from typing import Optional

import numpy as np
import pandas as pd
import json
from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.constant.database import DATABASE_NAME
from sensor.exception import SensorException

  
class SensorData:
    """
    This class help to export entire mongo db record as pandas dataframe
    """

    def __init__(self):
   
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)

        except Exception as e:
            raise SensorException(e, sys)


    def save_csv_file(self,file_path ,collection_name: str, database_name: Optional[str] = None):
        try:
            data_frame=pd.read_csv(file_path)
            data_frame.reset_index(drop=True, inplace=True)
            records = list(json.loads(data_frame.T.to_json()).values())
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
            collection.insert_many(records)
            return len(records)
        except Exception as e:
            raise SensorException(e, sys)
        

    def export_collection_as_dataframe(
    self, collection_name: str, database_name: Optional[str] = None, limit: int = 10000) -> pd.DataFrame:
     try:
        """
        Export limited collection as DataFrame to avoid MemoryError
        """
        if database_name is None:
            collection = self.mongo_client.database[collection_name]
        else:
            collection = self.mongo_client[database_name][collection_name]

        # Fetch only a limited number of documents
        cursor = collection.find().limit(limit)
        df = pd.DataFrame(list(cursor))

        if "_id" in df.columns:
            df.drop(columns=["_id"], inplace=True)

        df.replace({"na": np.nan}, inplace=True)

        return df

     except Exception as e:
        raise SensorException(e, sys)



   

