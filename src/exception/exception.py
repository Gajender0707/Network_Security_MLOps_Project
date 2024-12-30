import sys
import os
from src.logging.logging import Logger


def Error_details(e):
    tb_exc=sys.exc_info()[2]
    error_name=e
    file_name=tb_exc.tb_frame.f_code.co_filename
    lineno=tb_exc.tb_lineno
    
    error_detail=f"""An Error is Occured in python script at line no {lineno} and error is <<{error_name}>>
      in the file {file_name}"""
    
    return error_detail



class CustomException(Exception):
    "This is predefined class which will be used in custom Exception"

    def __init__(self,error):
        super().__init__(self,error)
        self.error=Error_details(error)
    def __str__(self) -> str:
        return self.error
    

# if __name__=="__main__":
#     try:
#         print(1/0)
#     except CustomException as e:
#         raise e