from src .exception.exception import CustomException
from src.logging.logging import Logger
from src.utils.common import make_dir,read_yaml
from src.entity.artifacts_entity import DataIngestionArtifacts
from src.entity.config_entity import TrainingPipelineConfig
from src.entity.config_entity import DataIngestionConfig
import pandas as pd
import numpy as np
import os
from pathlib import Path
from pymongo import MongoClient
from sklearn.model_selection import train_test_split
from dotenv import load_dotenv
import certifi


load_dotenv()

MONGO_DB_URI=os.getenv("MONGODB_URI")

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        self.data_ingestion_config=data_ingestion_config
        # self.client=MongoClient(MONGO_DB_URI)
        self.client=MongoClient("mongodb+srv://iamsanju0707:DWVLL5PqpDwtXOjl@cluster0.4ul2y.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
                                 tlsCAFile=certifi.where())
        Logger.info("DataIngestion Config Fetch Sucessfully..")


    def export_collection_to_dataframe(self):
        try:
            db=self.client[self.data_ingestion_config.database_name]
            # print(db)
            collection=db[self.data_ingestion_config.collection_name]
            # print(collection)
            documents=collection.find()
            # print(documents)
            Logger.info("Documemnts Extract Database Sucessfully...")
            documents_list = list(documents)
            # print(documents_list)
            df=pd.DataFrame(documents_list)
            Logger.info("Dataframe Create Successfully....")
            # print(df)
            # print(self.client.server_info())
            return df
        
        except Exception as e:
            raise CustomException(e)

        

    def export_df_into_feature_store(self):
        try:
            df=self.export_collection_to_dataframe()
            feature_store_path=Path(self.data_ingestion_config.feature_store_file_path)
            print(feature_store_path)
            make_dir(feature_store_path)
            df.to_csv(feature_store_path)
            Logger.info("Data Export to feature Store Sucessfully..")
        except Exception as e:
            raise CustomException(e)
        

    def split_data_into_train_and_test(self):
        try:
            df=self.export_collection_to_dataframe()
            test_size=self.data_ingestion_config.train_test_split_ratio
            train_data,test_data=train_test_split(df,test_size=test_size)
            Logger.info("Data has been splitted into the train and test Sucessfully..")
            train_data_path=self.data_ingestion_config.training_file_path
            test_data_path=self.data_ingestion_config.testing_file_path
            make_dir(Path(train_data_path))
            #training data 
            pd.DataFrame(train_data).to_csv(train_data_path,index=False,header=True)
            Logger.info("Trainning data has been saved Sucessfully..")

            #testing data
            pd.DataFrame(test_data).to_csv(test_data_path,index=False,header=True)
            Logger.info("Test data has been Saved Sucessfully.")

        except Exception as e:
            raise CustomException(e)


    def initiate_data_ingestion(self)-> DataIngestionArtifacts:
        try:
            self.export_df_into_feature_store()
            self.split_data_into_train_and_test()
            data_ingestion_artifacts=DataIngestionArtifacts(
                training_data_path=self.data_ingestion_config.training_file_path,
                testing_data_path=self.data_ingestion_config.testing_file_path
            )
            return data_ingestion_artifacts



        except Exception as e:
            raise CustomException(e)



if __name__=="__main__":
    training_pipeline_config=TrainingPipelineConfig()
    cofig=DataIngestionConfig(training_pipeline_config)
    obj=DataIngestion(cofig)
    data_ingestion_artifacts=obj.initiate_data_ingestion()
    print(data_ingestion_artifacts)
    # obj.export_collection_to_dataframe()