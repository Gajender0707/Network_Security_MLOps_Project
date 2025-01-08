from src.logging.logging import Logger
from src.entity.config_entity import DataTransformationConfig,DataValidationArtifact,DataValidationConfig,TrainingPipelineConfig
from src.components.data_transformation import DataTransformation
from src.pipeline.data_validation_pipeline import DataValidationPipeline

STAGE_NAME="<<<<<<< data transformation pipeline >>>>>>>>>>>>"
class DataTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation_pipeline(self):
        Logger.info(f"{STAGE_NAME} has been Started") 
        data_validation_pipeline_obj=DataValidationPipeline()
        data_validation_artifacts=data_validation_pipeline_obj.initiate_data_validation_pipeline()
        print(data_validation_artifacts)
        data_transformation_config=DataTransformationConfig()
        obj=DataTransformation(data_validation_artifacts,data_transformation_config)
        data_transformation_artifacts=obj.initiate_data_transformation()
        Logger.info(f"{STAGE_NAME} has been Done")
        return data_transformation_artifacts