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


#loading the Env Variables...
load_dotenv()
config_file_path=Path(os.getenv("CONFIG_YAML_PATH"))
mongodb_uri=os.getenv("MONGODB_URI")


class NetworkDataExtraction:

    def __init__(self,database_name,collection_name,
                 config_file_path=config_file_path,mongodb_uri=mongodb_uri
            ):
        try:
            self.mongodb_uri=mongodb_uri
            self.database_name=database_name
            self.collection_name=collection_name
            yaml_file_data=read_yaml(config_file_path)
            self.data_path=yaml_file_data.raw_data_details.data_file_path

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


if __name__=="__main__":
    obj=NetworkDataExtraction(database_name="Network_Security_Database",collection_name="NetworkData")
    obj.push_to_mongodb()