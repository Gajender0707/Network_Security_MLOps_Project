from src.entity.artifacts_entity import DataTransformationArtifact
from src.entity.config_entity import ModelTrainerConfig,TrainingPipelineConfig
from src.exception.exception import CustomException
from src.logging.logging import Logger
from src.utils.common import make_dir,read_yaml,save_object,load_array,load_object
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from src.pipeline.data_transformation_pipeline import DataTransformationPipeline
from pathlib import Path
from src.utils.ml_utils.model import model_evaluate,NetworkModel



class ModelTrainer:

    def __init__(self,data_transformation_artifacts:DataTransformationArtifact,
                 model_trainer_config:ModelTrainerConfig):
        self.data_transformation_artifacts=data_transformation_artifacts
        self.model_trainer_config=model_trainer_config

    def train_model(self,X_train,y_train,X_test,y_test):
        try:
            params_file_data=read_yaml(Path(self.model_trainer_config.params_config_file_path))
            models_params=params_file_data["models_params"]
            models=params_file_data["models"]
            models=dict(models)
  
            #model Evaluation
            model_report=model_evaluate(X_train,y_train,X_test,y_test,models,models_params)
            #now find out thte best model 
            best_score=max([  score for score in model_report.values()])
            best_model_name=[ model_name for model_name,model_score in model_report.items() if model_score==best_score ][0]
            best_model=eval([ model for model_name,model in models.items() if model_name==best_model_name][0])


            return best_model

        except Exception as e:
            raise CustomException(e)
        


    def initiate_model_trainer(self):
        try:
            train_data=load_array(self.data_transformation_artifacts.transformed_train_file_path)
            test_data=load_array(self.data_transformation_artifacts.transformed_test_file_path)
            X_train=train_data[:,:-1]
            y_train=train_data[:,-1]
            X_test=test_data[:,:-1]
            y_test=test_data[:,-1]

            best_model=self.train_model(X_train,y_train,X_test,y_test)
            best_model.fit(X_train,y_train)


            # y_train_pred=best_model.predict(X_train)

            # print(y_train_pred)


            #Preprocessor
            preprocessor=load_object(self.data_transformation_artifacts.transformed_object_file_path)

            Network_Model=NetworkModel(preprocessor,best_model)

            save_object(self.model_trainer_config.trained_model_file_path,best_model)
            Logger.info("Model has been saved Sucessfully...")



        except Exception as e:
            raise CustomException(e)
        

if __name__=="__main__":
    data_transforamtion_artifacts=DataTransformationPipeline().initiate_data_transformation_pipeline()
    # print(data_transforamtion_artifacts.initiate_data_transformation_pipeline())
    model_trainer_basic_config=TrainingPipelineConfig()
    model_trainer_config=ModelTrainerConfig(model_trainer_basic_config)
    obj=ModelTrainer(data_transforamtion_artifacts,model_trainer_config)
    res=obj.initiate_model_trainer()
    print(res)
