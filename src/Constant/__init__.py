import os
from pathlib import Path


#defining common contanst Variable which are important for the training pipeline

DATA_FILE_NAME="phisingData.csv"
ARTIFACTS_DIR="artifacts"

TRAIN_FILE_NAME="train.csv"
TEST_FILE_NAME="test.csv"


#Data Ingestion constant Variable which will used throughout the DataIngestion Process, Start with DATA_INGESTION keyword
DATA_INGESTION_DIR_NAME:str="data_ingestion"
DATA_INGESTION_DATABASE_NAME:str="Network_Security_Database"
DATA_INGESTION_COLLECTION_NAME:str="NetworkData"
DATA_INGESTION_INGESTED_DIR_NAME:str="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float=0.2






