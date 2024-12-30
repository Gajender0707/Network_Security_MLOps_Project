import os
from pathlib import Path
from src.logging.logging import Logger


list_of_files=[
    "src/__init__.py",

    #Components
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/data_validation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    
    #Pipelines
    "src/pipeline/__init__.py",
    "src/pipeline/data_ingestion_pipeline.py",
    "src/pipeline/data_transformation_pipeline.py",
    "src/pipeline/data_validation_pipeline.py",
    "src/pipeline/model_trainer_pipeline.py",
    "src/pipeline/model_evaluation_pipeline.py",

    #Config
    "Config/config.yaml",

    #Constant 
    "src/Constant/__init__.py",

    #Configuration
    "src/config/__init__.py",
    "src/config/configuration.py",

    #utils
    "src/utils/__init__.py",
    "src/utils/common.py",

    #entity
    "src/entity/__init__.py",
    "src/entity/config_entity.py",

    #cloud
    "src/cloud/__init__.py",
    

    #github actions workflow
    ".github/workflows/.gitkeep",

    #Templates
    "templates/index.html",

    #Notebook
    "research/reasearch.ipynb",

    #Logger and Exception
    "src/logging/__init__.py",
    "src/logging/logging.py",
    "src/exception/__init__.py",
    "src/exception/exception.py",

    ".env",
    "README.md",

    ".gitignore",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "Schema.yaml",
    "params.yaml",
    "main.py",
]

for file in list_of_files:
    file=Path(file)
    dirname,filename=os.path.split(file)
    print(dirname,filename)

    if dirname!="":
        os.makedirs(dirname,exist_ok=True)
        Logger.info("Directory Created Successfully....")

    if (not os.path.exists(file)) or (os.path.getsize(file)==0):
        with open(file,"w") as f:
            pass






