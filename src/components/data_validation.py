from src.entity.config_entity import DataValidationConfig
from src.entity.config_entity import TrainingPipelineConfig



if __name__=="__main__":
    training_pipeline_config=TrainingPipelineConfig()
    config=DataValidationConfig(training_pipeline_config)
    print(config.data_drift_report_file_path)