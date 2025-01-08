from src.entity.artifacts_entity import DataTransformationArtifact
from src.entity.config_entity import ModelTrainerConfig
from src.exception.exception import CustomException
from src.logging.logging import Logger
from src.utils.common import make_dir,read_yaml,save_object

class ModelTrainer:

    def __init__(self,data_transformation_artifacts:DataTransformationArtifact,
                 model_trainer_config:ModelTrainerConfig):
        self.data_transformation_artifacts=data_transformation_artifacts
        self.model_trainer_config=model_trainer_config


    def initiate_model_trainer(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e)