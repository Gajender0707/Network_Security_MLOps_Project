from src.logging.logging import Logger
from src.exception.exception import CustomException
from src.entity.config_entity import DataTransformationConfig, DataValidationConfig,TrainingPipelineConfig
from src.entity.artifacts_entity import DataTransformationArtifact
from src.utils.common import make_dir,read_yaml,save_array,save_object
import pandas   as pd
import numpy as np
from src.pipeline.data_validation_pipeline import DataValidationPipeline
from sklearn.pipeline import Pipeline
from sklearn.impute import KNNImputer
from pathlib import Path




class DataTransformation:

    def __init__(self,data_validation_artifacts,
                 data_transformation_config:DataTransformationConfig):
        try:
            self.data_validation_artifacts=data_validation_artifacts
            self.data_transforamtion_config=data_transformation_config
        except Exception as e:
            raise CustomException(e)
        
    #read the validate  data
    def read_data(self,filepath)->pd.DataFrame:
        try:
            df=pd.read_csv(filepath)
            return df
        except Exception as e:
            raise CustomException(e)
        
    
    def get_transformer_object(self)->Pipeline:
        try:
            Logger.info("Data Null values fill using the KNN imputer.")
            params=read_yaml(Path(self.data_transforamtion_config.params_file_path))
            knn_params=dict(params["knn_imputer_params"])
            imputer:KNNImputer=KNNImputer(**knn_params)
            preprocessor:Pipeline=Pipeline(steps=[
                ("imputer",imputer)
            ])
            Logger.info("Preprocessing pipeline has been added with knn imputer for handling the null values..")
            return preprocessor

        except Exception as e:
            raise CustomException(e)


    def initiate_data_transformation(self)-> DataTransformationArtifact:
        try:
            # print(self.data_validation_artifacts.valid_train_file_path)
            valid_train_df=self.read_data(self.data_validation_artifacts.valid_train_file_path)
            valid_test_df=self.read_data(self.data_validation_artifacts.valid_test_file_path)

            #define target column
            target_column=self.data_transforamtion_config.target_column
            # print(target_column_name)

            
            # make train data ready or the preprocessing steps..
            input_features_train=valid_train_df.drop(columns=[target_column],axis=1)
            target_feature_train=valid_train_df[target_column].replace(-1,0)


            #make test data ready for the preprocessing steps...
            input_features_test=valid_test_df.drop(columns=[target_column],axis=1)
            target_feature_test=valid_test_df[target_column].replace(-1,0)


            preprocessor=self.get_transformer_object()
            Logger.info("Fitting the Preprocessor with train data...")
            #fit the train data with the preprocessor..
            preprocessor_obj=preprocessor.fit(input_features_train)


            #transform the data using the preprocessor
            processed_train_features=preprocessor_obj.transform(input_features_train)
            processed_test_features=preprocessor_obj.transform(input_features_test)


            ## now again concate the train and test features and target

            train_arr=np.c_[processed_train_features,np.array(target_feature_train)]
            test_arr=np.c_[processed_test_features,np.array(target_feature_test)]


            ## now save the  preprocessed and transformed array in the data transformation artifacts 
            save_array(self.data_transforamtion_config.transformed_train_file_path,train_arr)
            save_array(self.data_transforamtion_config.transformed_test_file_path,test_arr)

            #save the preprocessor
            save_object(self.data_transforamtion_config.transformed_object_file_path,preprocessor_obj)


            data_transform_artifacts=DataTransformationArtifact(
                transformed_train_file_path=self.data_transforamtion_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transforamtion_config.transformed_test_file_path,
                transformed_object_file_path=self.data_transforamtion_config.transformed_object_file_path
            )

            return data_transform_artifacts
        
        except Exception as e:
            raise CustomException(e)




# if __name__=="__main__":
#     data_validation_pipeline_obj=DataValidationPipeline()
#     data_validation_artifacts=data_validation_pipeline_obj.initiate_data_validation_pipeline()
#     print(data_validation_artifacts)
#     data_transformation_config=DataTransformationConfig()
#     obj=DataTransformation(data_validation_artifacts,data_transformation_config)
#     res=obj.initiate_data_transformation()
#     print(res)