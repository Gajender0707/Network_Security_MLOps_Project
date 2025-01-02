import os
from pathlib import Path


#defining common contanst Variable which are important for the training pipeline

DATA_FILE_NAME="phisingData.csv"
ARTIFACTS_DIR="artifacts"

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







