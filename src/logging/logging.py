import os
import sys
import logging


logging_format='%(asctime)s - %(levelname)s -%(module)s - %(message)s'

logging_dir="Logs"

logging_filepath=os.path.join(logging_dir,"logging.log")
os.makedirs(logging_dir,exist_ok=True)

logging.basicConfig(
    format=logging_format,
    level=logging.INFO,
    handlers=[
        logging.FileHandler(logging_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)


Logger=logging.getLogger("Data_Science_Logger")