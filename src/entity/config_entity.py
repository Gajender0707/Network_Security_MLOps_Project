import os
from pathlib import Path
from src.Constant import training_pipeline
from datetime import datetime
from src.utils.common import make_dir

#this training pipeline is the common for all the further configuration
class TrainingPipelineConfig:
    def __init__(self):
        self.artifacts_dir=training_pipeline.ARTIFACTS_DIR



class DataIngestionConfig:
    def __init__(self,data_ingestion_config:TrainingPipelineConfig):
        self.data_ingestion_config=data_ingestion_config
        self.data_ingestion_dir=os.path.join(self.data_ingestion_config.artifacts_dir,training_pipeline.DATA_INGESTION_DIR_NAME)
        # make_dir(self.data_ingestion_dir)
        self.feature_store_file_path:str=os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INGSTION_FEATURE_STORE_DIR_NAME,
                                                      training_pipeline.DATA_FILE_NAME)
        # make_dir(self.feature_store_file_path)
        self.training_file_path:str=os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR_NAME,
                                                 training_pipeline.TRAIN_FILE_NAME)
        
        #Testing data
        self.testing_file_path:str=os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR_NAME,
                                                training_pipeline.TEST_FILE_NAME)
        
        self.train_test_split_ratio=training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        self.database_name=training_pipeline.DATA_INGESTION_DATABASE_NAME
        self.collection_name=training_pipeline.DATA_INGESTION_COLLECTION_NAME

        


# if __name__=="__main__":
#     training_config=TrainingPipelineConfig()
#     obj=DataIngestionConfig(training_config)
#     print(obj.feature_store_file_path)
        





