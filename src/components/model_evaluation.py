from src.logging.logging import Logger
from src.exception.exception import CustomException
from src.entity.config_entity import ModelEvaluationConfig,TrainingPipelineConfig
from src.entity.artifacts_entity import ModelTrainerArtifacts
from src.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.utils.common import load_object,load_array
from src.utils.ml_utils.metric import get_classification_score


class ModelEvaluation:

    def __init__(self,model_trainer_artifacts:ModelTrainerArtifacts,
                 model_evaluation_config:ModelEvaluationConfig):
        self.model_trainer_artifacts=model_trainer_artifacts
        self.model_evaluation_config=model_evaluation_config


    def initiate_model_evaluation(self):
        try:
            print(f"This is model path {self.model_trainer_artifacts.trained_model_file_path}")
            print(f"this is the test file path{self.model_trainer_artifacts.test_data_file_path}")

        except Exception as e:
            raise CustomException(e)
        

if __name__=="__main__":
    model_trainer_obj=ModelTrainerPipeline()
    model_trainer_artifacts=model_trainer_obj.initiate_model_trainer_pipeline()
    basic_config=TrainingPipelineConfig()
    model_evaluation_config=ModelEvaluationConfig(basic_config)
    model_evaluation_obj=ModelEvaluation(model_trainer_artifacts,model_evaluation_config)
    res=model_evaluation_obj.initiate_model_evaluation()
    print(res)
        


