from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig,DataValidationConfig
from src.components.data_validation import DataValidation
from src.logging.logging import Logger
from src.pipeline.data_ingestion_pipeline import DataIngestionPipeline



STAGE_NAME="<<<<<<<<<<<<<< Data Validation Pipeline >>>>>>>>>>>>>>>>>>>>"
class DataValidationPipeline:
    def __init__(self):
        pass

    def initiate_data_validation_pipeline(self):
            Logger.info(f"{STAGE_NAME} has been Started")
            data_ingestion_pipeline_obj=DataIngestionPipeline()
            data_ingestion_artifacts=data_ingestion_pipeline_obj.initiate_data_ingestion_pipeline()
            training_pipeline_config=TrainingPipelineConfig()
            data_validation_config=DataValidationConfig(training_pipeline_config)
            obj=DataValidation(data_validation_config,data_ingestion_artifacts)
            data_validation_artifacts=obj.initiate_data_validation()
            Logger.info(f"{STAGE_NAME} has been Done")
            return data_validation_artifacts