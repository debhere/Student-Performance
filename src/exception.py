import sys
from src.logger import logging

def exception_details(error, error_detail:sys) -> str:
    _,_,exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in {filename}, line number {exc_tb.tb_lineno}: str(error)"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = exception_details(error_message, error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
