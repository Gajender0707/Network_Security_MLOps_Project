import os
from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionArtifacts:
    training_data_path:Path
    testing_data_path:Path


@dataclass
class DataValidationArtifact:
    validation_status: bool
    valid_train_file_path: str
    valid_test_file_path: str
    invalid_train_file_path: str
    invalid_test_file_path: str
    drift_report_file_path: str



@dataclass
class DataTransformationArtifact:
    transformed_train_file_path:str
    transformed_test_file_path:str
    transformed_object_file_path:str


@dataclass
class ModelTrainerArtifacts:
    trained_model_file_path:str
    train_data_file_path:str
    test_data_file_path:str



# @dataclass
# class ClassificationMetricArtifact:
#     f1_score:float
#     precision_score:float
#     recall_score:float
#     accuracy_score:float



@dataclass
class ModelEvaluationArtifacts:
    train_metric_file_path:str
    test_metric_file_path:str