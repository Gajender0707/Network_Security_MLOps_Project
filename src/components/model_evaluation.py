from src.logging.logging import Logger
from src.exception.exception import CustomException
from src.entity.config_entity import ModelEvaluationConfig,TrainingPipelineConfig
from src.entity.artifacts_entity import ModelTrainerArtifacts,ModelEvaluationArtifacts
from src.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.utils.common import load_object,load_array,save_json,save_object
from src.utils.ml_utils.metric import get_classification_score
from dotenv import load_dotenv
import mlflow
import os
from urllib.parse import urlparse

load_dotenv()
os.getenv("MLFLOW_TRACKING_URI")
os.getenv("MLFLOW_TRACKING_USERNAME")
os.getenv("MLFLOW_TRACKING_PASSWORD")


class ModelEvaluation:

    def __init__(self,model_trainer_artifacts:ModelTrainerArtifacts,
                 model_evaluation_config:ModelEvaluationConfig):
        self.model_trainer_artifacts=model_trainer_artifacts
        self.model_evaluation_config=model_evaluation_config


    def mlflow_tracking(self,classification_report,best_model):
        try:
            mlflow.set_registry_uri(os.getenv("MLFLOW_TRACKING_URI"))
            tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
            # mlflow.set_experiment("My_Custom_Experiment")
            with mlflow.start_run():
                f1_score=float(classification_report["f1_score"])
                precision_score=float(classification_report["precision_score"])
                recall_score=float(classification_report["recall_score"])
                accuracy_score=float(classification_report["accuracy_score"])

                #logging the metrics
                mlflow.log_metric("f1 score",f1_score)
                mlflow.log_metric("precision score",precision_score)
                mlflow.log_metric("recall score",recall_score)
                mlflow.log_metric("accuracy score",accuracy_score)


                #logging the model
                if tracking_url_type_store!="file":
                    mlflow.sklearn.log_model(best_model,"model",registered_model_name="best_model")
                else:
                    mlflow.sklearn.log_model(best_model,"model")


        except Exception as e:
            raise CustomException(e)


    def initiate_model_evaluation(self) -> ModelEvaluationArtifacts:
        try:
            model=load_object(self.model_trainer_artifacts.trained_model_file_path)
            
            train_arr=load_array(self.model_trainer_artifacts.train_data_file_path)
            test_arr=load_array(self.model_trainer_artifacts.test_data_file_path)

            

            X_train=train_arr[:,:-1]
            X_test=test_arr[:,:-1]

            y_train_true=train_arr[:,-1]
            y_test_true=test_arr[:,-1]

            y_train_pred=model.predict(X_train)
            y_test_pred=model.predict(X_test)

            train_classification_report=get_classification_score(y_train_true,y_train_pred)
            #tracking for the training report 
            self.mlflow_tracking(train_classification_report,model)



            test_classification_report=get_classification_score(y_test_true,y_test_pred)
            #tracking for the testing report
            self.mlflow_tracking(test_classification_report,model)



            ##Now save the metrics report to the model evaluation artifacts

            #save the train metrics
            save_json(self.model_evaluation_config.train_metric_file_path,train_classification_report)

            #save the test metrics
            save_json(self.model_evaluation_config.test_metric_file_path,test_classification_report)



            
            

            model_evaluation_artifacts=ModelEvaluationArtifacts(
                train_metric_file_path=self.model_evaluation_config.train_metric_file_path,
                test_metric_file_path=self.model_evaluation_config.test_metric_file_path)
            
            return model_evaluation_artifacts
            

        except Exception as e:
            raise CustomException(e)
        


# if __name__=="__main__":
#     model_trainer_obj=ModelTrainerPipeline()
#     model_trainer_artifacts=model_trainer_obj.initiate_model_trainer_pipeline()
#     basic_config=TrainingPipelineConfig()
#     model_evaluation_config=ModelEvaluationConfig(basic_config)
#     model_evaluation_obj=ModelEvaluation(model_trainer_artifacts,model_evaluation_config)
#     res=model_evaluation_obj.initiate_model_evaluation()
#     print(res)
        


