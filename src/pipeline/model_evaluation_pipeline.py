from src.logging.logging import Logger
from src.exception.exception import CustomException
from src.entity.config_entity import ModelEvaluationConfig


class ModelEvaluation:

    def __init__(self):
        pass


    def initiate_model_evaluation(self):
        try:
            pass

        except Exception as e:
            raise CustomException(e)
        

if __name__=="__main__":
    obj=ModelEvaluation()
    res=obj.initiate_model_evaluation()
    print(res)
        


