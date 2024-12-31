from dotenv import load_dotenv
import os
import pandas as pd
from src.utils.common import read_yaml
from src.logging.logging import Logger
from src.exception.exception import CustomException
from pathlib import Path
import json
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from src.Constant import DATA_FILE_NAME


#loading the Env Variables...
load_dotenv()
mongodb_uri=os.getenv("MONGODB_URI")


class NetworkDataExtraction:

    def __init__(self,database_name,collection_name,
                 mongodb_uri=mongodb_uri,data_file_path=DATA_FILE_NAME
            ):
        try:
            self.mongodb_uri=mongodb_uri
            self.database_name=database_name
            self.collection_name=collection_name
            self.data_path=data_file_path

        except Exception as e:
            raise CustomException(e)

    def csv_to_json_convertor(self):
        try:
            data=pd.read_csv(self.data_path)
            records=data.to_dict(orient="records")
            # print(type(records))
            return records
        except Exception as e:
            raise CustomException(e)


    def push_to_mongodb(self):
        try:
            records=self.csv_to_json_convertor()
            # client = MongoClient(self.mongodb_uri, server_api=ServerApi('1'))
            client=MongoClient(self.mongodb_uri)
            database=client[self.database_name]
            collection=database[self.collection_name]
            collection.insert_many(records)
            Logger.info("Data Push to MongoDB Sucessfully...")

        except Exception as e:
            raise CustomException(e)


# if __name__=="__main__":
#     obj=NetworkDataExtraction(database_name="Network_Security_Database",collection_name="NetworkData")
#     obj.push_to_mongodb()
