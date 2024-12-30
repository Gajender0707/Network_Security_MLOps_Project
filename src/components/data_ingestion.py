from src .exception.exception import CustomException

try:
    print(1/0)
except Exception as e:
    raise CustomException(e)