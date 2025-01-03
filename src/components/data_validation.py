from src.entity.config_entity import DataValidationConfig
from src.entity.config_entity import TrainingPipelineConfig
from src.exception.exception import CustomException
from src.logging.logging import Logger
from src.utils.common import make_dir,read_yaml
import pandas as pd
from src.entity.artifacts_entity import DataIngestionArtifacts
from pathlib import Path



class DataValidation:
    def __init__(self,data_validation_config:DataValidationConfig,data_ingestion_artifacts:DataIngestionArtifacts):
        self.data_validation_config=data_validation_config
        self.data_ingestion_artifacts=data_ingestion_artifacts


    #reading the data from the artifacts
    def read_data(self):
        try:
            df=pd.read_csv(self.data_ingestion_artifacts.training_data_path)
            return df
        except Exception as e:
            raise CustomException(e)
    

    #validating the number of columns which match with schema..
    def validate_number_of_columns(self):
        try:
            schema=read_yaml(Path(self.data_validation_config.schema_file_path))
            df=self.read_data()
            if len(schema)==len(df.columns):
                True
            return False

        except Exception as e:
            raise CustomException(e)
        
    
    

    #initiating the Data Validtion...
    def initiate_data_validation(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e)



from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import DataIngestionConfig
if __name__=="__main__":

    #data ingestion pipeline
    training_pipeline_config=TrainingPipelineConfig()
    cofig=DataIngestionConfig(training_pipeline_config)
    obj=DataIngestion(cofig)
    data_ingestion_artifacts=obj.initiate_data_ingestion()
    #validation pipeline
    training_pipeline_config=TrainingPipelineConfig()
    data_validation_config=DataValidationConfig(training_pipeline_config)
    obj=DataValidation(data_validation_config,data_ingestion_artifacts)
    obj.validate_number_of_columns()