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





# if __name__=="__main__":
#     filepath=os.getenv("CONFIG_YAML_PATH")
#     data=read_yaml(Path(filepath))
#     print(data)


