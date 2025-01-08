from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig
from src.logging.logging import Logger


STAGE_NAME="<<<<<<<<<<<<<< Data Ingestion Pipeline >>>>>>>>>>>>>>>>>>>>"
class DataIngestionPipeline:
    def __init__(self):
        pass
    def initiate_data_ingestion_pipeline(self):
            Logger.info(f"{STAGE_NAME} has been Started")
            training_pipeline_config=TrainingPipelineConfig()
            cofig=DataIngestionConfig(training_pipeline_config)
            obj=DataIngestion(cofig)
            data_ingestion_artifacts=obj.initiate_data_ingestion()
            Logger.info(f"{STAGE_NAME} has been Done")
            return data_ingestion_artifacts


