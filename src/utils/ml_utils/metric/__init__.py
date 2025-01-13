from src.exception.exception import CustomException
from src.logging.logging import Logger
from sklearn.metrics import f1_score,precision_score,recall_score,accuracy_score
import json


def get_classification_score(y_true,y_pred):
    try:
        f1score=f1_score(y_true,y_pred)
        p_score=precision_score(y_true,y_pred)
        r_score=recall_score(y_true,y_pred)
        acc_score=accuracy_score(y_true,y_pred)

        classification_score={
            "f1_score":f1score,
            "precision_score":p_score,
            "recall_score":r_score,
            "accuracy_score":acc_score
        }

        return classification_score
    
    except Exception as e:
        raise CustomException(e)
