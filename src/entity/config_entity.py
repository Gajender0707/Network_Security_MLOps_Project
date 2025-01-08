import os
from pathlib import Path
from src.Constant import training_pipeline
from src.entity.artifacts_entity import DataValidationArtifact
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


class DataValidationConfig:

    def __init__(self,data_validation_config:TrainingPipelineConfig):
        self.data_validation_config=data_validation_config
        ## Valid data Configuration
        self.data_validation_dir=os.path.join(self.data_validation_config.artifacts_dir,training_pipeline.DATA_VALIDATION_DIR)
        self.valid_train_file_path=os.path.join(self.data_validation_dir,training_pipeline.DATA_VALIDATION_VALID_DATA_DIR,
                                               training_pipeline.TRAIN_FILE_NAME)
        self.valid_test_file_path=os.path.join(self.data_validation_dir,training_pipeline.DATA_VALIDATION_VALID_DATA_DIR,
                                               training_pipeline.TEST_FILE_NAME)
        
        #invalid_data_configuration
        self.invalid_train_file_path=os.path.join(self.data_validation_dir,training_pipeline.DATA_VALIDATION_INVALID_DATA_DIR,
                                                  training_pipeline.TRAIN_FILE_NAME)
        self.invalid_test_file_path=os.path.join(self.data_validation_dir,training_pipeline.DATA_VALIDATION_INVALID_DATA_DIR,
                                                 training_pipeline.TEST_FILE_NAME)
        self.data_drift_report_file_path=os.path.join(self.data_validation_dir,training_pipeline.DATA_VALIDATION_DRIFT_REPORT_FILE_DIR,
                                                      training_pipeline.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME)
        self.schema_file_path=training_pipeline.SCHEMA_FILE_PATH
        



class DataTransformationConfig:

    def __init__(self):
        self.target_column=training_pipeline.TARGET_COLUMN
        #data transformation dir
        self.data_transformation_dir=os.path.join(training_pipeline.ARTIFACTS_DIR,training_pipeline.DATA_TRANSFORMATION_DIR)

        #transformed data dir
        self.transformed_data_dir=os.path.join(self.data_transformation_dir,training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR)

        # transformed train file path
        self.transformed_train_file_path=os.path.join(self.transformed_data_dir,
                                                      training_pipeline.TRAIN_FILE_NAME.replace(".csv",".npy"))
        
        #transformed test data file path
        self.transformed_test_file_path=os.path.join(self.transformed_data_dir,
                                                      training_pipeline.TEST_FILE_NAME.replace(".csv",".npy"))
        

        #transformed object file path

        self.transformed_object_file_path=os.path.join(self.transformed_data_dir,training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,
                                                       training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_OBJECT_FILE_NAME)
        
        # params file path
        self.params_file_path=training_pipeline.DATA_TRANSFORMATION_PARAMS_FILE_PATH


        


# if __name__=="__main__":
#     # training_config=TrainingPipelineConfig()
#     obj=DataTransformationConfig()
#     print(obj.transformed_train_file_path)
        





