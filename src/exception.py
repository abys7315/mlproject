import sys
##error_detail:sys means error_detail is type of sys
def error_message_detail(error,error_detail:sys):
    exc_type,exc_value,exc_tb=error_detail.exc_info()##exc_info() will tell about the execution info
    ##exc_tb will give where the error happened like file name,line number,function name
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="error occured in python script name [{0}] line number [{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    
    return error_message
    
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
        
    def __str__(self):
        return self.error_message
        