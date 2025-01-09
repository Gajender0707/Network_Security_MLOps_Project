from src.exception.exception import CustomException
from src.logging.logging import Logger
from src.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.entity.config_entity import TrainingPipelineConfig,ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

STAGE_NAME="<<<<<<< Model Trainer Pipeline >>>>>>>>>>>>"
class ModelTrainerPipeline:

    def __init__(self):
        pass


    def initiate_model_trainer_pipeline(self):
        try:
            Logger.info(f"{STAGE_NAME} has been Started") 
            data_transforamtion_artifacts=DataTransformationPipeline().initiate_data_transformation_pipeline()
            model_trainer_basic_config=TrainingPipelineConfig()
            model_trainer_config=ModelTrainerConfig(model_trainer_basic_config)
            obj=ModelTrainer(data_transforamtion_artifacts,model_trainer_config)
            model_trainer_artifacts=obj.initiate_model_trainer()
            Logger.info(f"{STAGE_NAME} has been Done")
            return model_trainer_artifacts
        
        except Exception as e:
            raise CustomException(e)