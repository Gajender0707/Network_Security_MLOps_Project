import os
from pathlib import Path


#defining common contanst Variable which are important for the training pipeline

DATA_FILE_NAME="phisingData.csv"
ARTIFACTS_DIR="artifacts"
TARGET_COLUMN="Result"


TRAIN_FILE_NAME="train.csv"
TEST_FILE_NAME="test.csv"
SCHEMA_FILE_PATH:str="schema.yaml"


#Data Ingestion constant Variable which will used throughout the DataIngestion Process, Start with DATA_INGESTION keyword
DATA_INGESTION_DIR_NAME:str="data_ingestion"
DATA_INGESTION_DATABASE_NAME:str="Network_Security_Database"
DATA_INGESTION_COLLECTION_NAME:str="NetworkData"
DATA_INGESTION_INGESTED_DIR_NAME:str="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float=0.2
DATA_INGSTION_FEATURE_STORE_DIR_NAME:str="feature_store"


#Data validation Constant variable for the validate the data for the further processing.
DATA_VALIDATION_DIR:str="data_validation"
DATA_VALIDATION_VALID_DATA_DIR:str="valid_data"
DATA_VALIDATION_INVALID_DATA_DIR:str="invalid_data"
DATA_VALIDATION_DRIFT_REPORT_FILE_DIR:str="data_drift"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str="report.yaml"


#Data Transformation Constant Variables which are must for the data transformation...
DATA_TRANSFORMATION_DIR:str="data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR:str="transformed"
DATA_TRANSFORMATION_TRAIN_DATA_FILE:str="train.npy"
DATA_TRANSFORMATION_TEST_DATA_FILE:str="test.npy"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR:str="transformed_object"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_FILE_NAME:str="preprocessor.pkl"
DATA_TRANSFORMATION_PARAMS_FILE_PATH:str="/Users/sanju/Documents/DS/MLOps/MLOps_Projects/Network_Security_Project/params.yaml"



#Model Trainer Constant varibles which are must for the model trainer
MODEL_TRAINER_DIR:str="model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR:str="trained_model"
MODEL_TRAINER_TRAINED_MODEL_FILE:str="model.pkl"


#Model Evaluation Contants
MODEL_EVALUATION_DIR:str="model_evaluation"
MODEL_EVALUATION_TRAIN_METRIC_DIR:str="train_metrics"
MODEL_EVALUATION_TEST_METRIC_DIR:str="test_metrics"
MODEL_EVALUATION_TRAIN_METRIC_FILE_PATH:str="train_metric.json"
MODEL_EVALUATION_TEST_METRIC_FILE_PATH:str="test_metric.json"



#Final Artifacts
FINAL_ARTIFACTS_PREPROCESSOR_FILE_PATH:str="final_artifacts/preprocessor.pkl"
FINAL_ARTIFACTS_MODEL_FILE_PATH:str="final_artifacts/model.pkl"




