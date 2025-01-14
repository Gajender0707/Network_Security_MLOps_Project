from src.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.pipeline.data_validation_pipeline import DataValidationPipeline
from src.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline
from src.exception.exception import CustomException


class Train_pipeline:
    
    def __init__(self):
        pass

    def start_training_pipeline(self):
        try:
            #Data Ingestion Pipeline
            data_ingestion_pipeline_obj=DataIngestionPipeline()
            data_ingestion_artifacts=data_ingestion_pipeline_obj.initiate_data_ingestion_pipeline()
            # print(data_ingestion_artifacts)


            #Data Validation Pipeline
            data_validation_pipeline_obj=DataValidationPipeline()
            data_validation_artifacts=data_validation_pipeline_obj.initiate_data_validation_pipeline()
            # print(data_validation_artifacts)



            #Data Transformation Pipeline
            data_transformation_pipeline_obj=DataTransformationPipeline()
            data_transformation_artifacsts=data_transformation_pipeline_obj.initiate_data_transformation_pipeline()
            # print(data_transformation_artifacsts)



            #Model Trainer Pipeline
            model_trainer_pipeline_obj=ModelTrainerPipeline()
            model_trainer_artifacts=model_trainer_pipeline_obj.initiate_model_trainer_pipeline()
            # print(model_trainer_artifacts)


            # Model Evaluation Pipeline
            model_evaluation_pipeline_obj=ModelEvaluationPipeline()
            model_evaluation_artifacts=model_evaluation_pipeline_obj.initiate_model_evaluation_pipeline()
            # print(model_evaluation_artifacts)

            return model_evaluation_artifacts

        except Exception as e:
            raise CustomException(e)
        


