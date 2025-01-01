from src.logging.logging import Logger
from src.exception.exception import CustomException
import yaml
from ensure import ensure_annotations
import os
from pathlib import Path
from dotenv import load_dotenv
from dotmap import DotMap

load_dotenv()


#method for reading the yaml files
@ensure_annotations
def read_yaml(filepath:Path):
    with open(filepath,"r") as f:
        data=yaml.safe_load(f)
        filedata=DotMap(data)
        Logger.info(f"Yaml file has been read Successfully. ")
    return filedata


@ensure_annotations
def make_dir(filepath:Path):
    dirpath,file_name=os.path.split(filepath)
    os.makedirs(dirpath,exist_ok=True)
    Logger.info(f"New Directory has been created on the Location {dirpath}.")


# make_dir(Path("/Users/sanju/Documents/DS/MLOps/MLOps_Projects/Network_Security_Project/data/phisingData.csv"))








# if __name__=="__main__":
#     filepath=os.getenv("CONFIG_YAML_PATH")
#     data=read_yaml(Path(filepath))
#     print(data)


