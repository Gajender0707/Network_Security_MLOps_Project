from src.exception.exception import CustomException
from src.logging.logging import Logger
from src.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.entity.config_entity import TrainingPipelineConfig,ModelEvaluationConfig
from src.components.model_evaluation import ModelEvaluation

STAGE_NAME="<<<<<<< Model Evaluation Pipeline >>>>>>>>>>>>"
class ModelEvaluationPipeline:

    def __init__(self):
        pass


    def initiate_model_evaluation_pipeline(self):
        try:
            Logger.info(f"{STAGE_NAME} has been Started") 
            model_trainer_obj=ModelTrainerPipeline()
            model_trainer_artifacts=model_trainer_obj.initiate_model_trainer_pipeline()
            basic_config=TrainingPipelineConfig()
            model_evaluation_config=ModelEvaluationConfig(basic_config)
            model_evaluation_obj=ModelEvaluation(model_trainer_artifacts,model_evaluation_config)
            model_evaluation_artifacts=model_evaluation_obj.initiate_model_evaluation()
            Logger.info(f"{STAGE_NAME} has been Done")
            return model_evaluation_artifacts
        
        except Exception as e:
            raise CustomException(e)