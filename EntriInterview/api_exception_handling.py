from rest_framework import exceptions


class APIException(exceptions.APIException):
   
    def __init__(self, detail=None, error_code=-1, kw=None):
        if isinstance(kw, dict):
            detail = detail % kw
        super(APIException, self).__init__(detail=detail)
        self.error_code = error_code
        self.message = detail


class ValidationError(APIException):
 
    status_code = 400
