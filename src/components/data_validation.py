from src.entity.config_entity import DataValidationConfig
from src.entity.config_entity import TrainingPipelineConfig
from src.exception.exception import CustomException
from src.logging.logging import Logger
from src.utils.common import make_dir,read_yaml,write_yaml
import pandas as pd
from src.entity.artifacts_entity import DataIngestionArtifacts,DataValidationArtifact
from pathlib import Path
from scipy.stats import ks_2samp



class DataValidation:
    def __init__(self,data_validation_config:DataValidationConfig,data_ingestion_artifacts:DataIngestionArtifacts):
        self.data_validation_config=data_validation_config
        self.data_ingestion_artifacts=data_ingestion_artifacts


    #reading the data from the artifacts
    def read_data(self,filepath:Path)-> pd.DataFrame:
        try:
            df=pd.read_csv(filepath)
            return df
        except Exception as e:
            raise CustomException(e)
    

    #validating the number of columns which match with schema..
    def validate_number_of_columns(self,df:pd.DataFrame):
        try:
            schema=read_yaml(Path(self.data_validation_config.schema_file_path))
            df=df
            # print(len(schema.columns))
            # print(len(df.columns))
            if len(schema.columns)==len(df.columns):
                Logger.info("DataFrame Columns has been validated Sucessfully.")
                return True
            return False

        except Exception as e:
            raise CustomException(e)
        

    def detect_dataset_drift(self,data1,data2,threshold_value=0.5):
        try:
            data_drift_report={}
            status=None
            for column in data1.columns:
                d1=data1[column]
                d2=data2[column]
                # print(f"this si d1: {d1}")
                # print(f"This is d2: {d2}")
                is_same_dist=ks_2samp(d1,d2)
                if is_same_dist.pvalue>0.05:
                    status=True
                else:
                    status=False
                data_drift_report.update({column:{
                    "report_status":status,
                    "p_value":float(is_same_dist.pvalue)
                }})
            return data_drift_report
        
        except Exception as e:
            raise CustomException(e)


    #initiating the Data Validtion...
    def initiate_data_validation(self)-> DataValidationArtifact:
        try:
            make_dir(Path(self.data_validation_config.data_validation_dir))
            df=self.read_data(self.data_ingestion_artifacts.training_data_path)
            status=self.validate_number_of_columns(df)
            Logger.info(f"Status Updated Sucessfully..  and Status is {status}")
            if status==True:
                message="Number of Features are Equal to  schema features"
                Logger.info(message)
                #validate train data inseration
                train_data_set=self.read_data(self.data_ingestion_artifacts.training_data_path)
                make_dir(Path(self.data_validation_config.valid_train_file_path))
                train_data_set.to_csv(self.data_validation_config.valid_train_file_path,header=True,index=False)
                Logger.info("Validated Training data has been saved...")

                #validate test data inseration
                test_data_set=self.read_data(self.data_ingestion_artifacts.testing_data_path)
                make_dir(Path(self.data_validation_config.valid_test_file_path))
                test_data_set.to_csv(self.data_validation_config.valid_test_file_path,header=True,index=False)
                Logger.info("Validated Test data has been saved...")
            else:

                message="Number of Features are Not Equal to  schema features"
                Logger.info(message)
                #validate train data inseration
                train_data_set=self.read_data(self.data_ingestion_artifacts.training_data_path)
                make_dir(Path(self.data_validation_config.invalid_train_file_path))
                train_data_set.to_csv(self.data_validation_config.invalid_train_file_path,header=False,index=False)
                Logger.info("InValidated Training data has been saved...")

                #validate test data inseration
                test_data_set=self.read_data(self.data_ingestion_artifacts.testing_data_path)
                make_dir(Path(self.data_validation_config.invalid_test_file_path))
                test_data_set.to_csv(self.data_validation_config.invalid_test_file_path,header=False,index=False)
                Logger.info("InValidated Test data has been saved...")

            #data drift Report updation
            data_drift_update_report=self.detect_dataset_drift(train_data_set,test_data_set)
            yaml_file_path=Path(self.data_validation_config.data_drift_report_file_path)
            yaml_file_path.parent.mkdir(parents=True, exist_ok=True)
            write_yaml(yaml_file_path,data_drift_update_report)
            
            Logger.info("Data Drift Report has been Updated...")

            data_validation_artifacts=DataValidationArtifact(
                validation_status=status,
                valid_train_file_path=self.data_validation_config.valid_train_file_path,
                valid_test_file_path=self.data_validation_config.valid_test_file_path,
                invalid_train_file_path=None,
                invalid_test_file_path=None,
                drift_report_file_path=self.data_validation_config.data_drift_report_file_path
            )
            return data_validation_artifacts

        except Exception as e:
            raise CustomException(e)



# from src.components.data_ingestion import DataIngestion
# from src.entity.config_entity import DataIngestionConfig
# if __name__=="__main__":

#     #data ingestion pipeline
#     training_pipeline_config=TrainingPipelineConfig()
#     cofig=DataIngestionConfig(training_pipeline_config)
#     obj=DataIngestion(cofig)
#     data_ingestion_artifacts=obj.initiate_data_ingestion()
#     #validation pipeline
#     training_pipeline_config=TrainingPipelineConfig()
#     data_validation_config=DataValidationConfig(training_pipeline_config)
#     obj=DataValidation(data_validation_config,data_ingestion_artifacts)
#     data_validation_artifacts=obj.initiate_data_validation()
#     print(data_validation_artifacts)