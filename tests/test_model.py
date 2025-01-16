# from src.logging.logging import Logger
# from src.exception.exception import CustomException
from src.Constant.training_pipeline import FINAL_ARTIFACTS_PREPROCESSOR_FILE_PATH,FINAL_ARTIFACTS_MODEL_FILE_PATH
from src.utils.ml_utils.model import NetworkModel
from src.utils.common import load_object
import numpy as np
import pandas as pd



def test_model_prediction():
    preprocessor=load_object(FINAL_ARTIFACTS_PREPROCESSOR_FILE_PATH)
    model=load_object(FINAL_ARTIFACTS_MODEL_FILE_PATH)
    model=NetworkModel(preprocessor,model)
    sample_data=np.array([[ 1, -1,  1,  1,  1,  1, -1,  1, -1, -1, -1,  1,  1,  0,  1, -1,
        -1,  1,  0,  1,  1, -1, -1,  1, -1,  1, -1,  1,  1, -1]])
    prediction_output=int(model.predict(sample_data)[0])
    actual_output=1
    assert prediction_output==actual_output, f"Expected {actual_output} but got {prediction_output}"


# test_model_prediction()
