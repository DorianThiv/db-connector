
class RequestFormatModelError(Exception):
    pass

class RequestFormatModel:
    """Request Builder have a specific format

    It can be understand by the other classes
    """
    pass

class RequestBuilder:
    """RequestBuilder static class provide Builders

    It be able to build a request from formatted data as a 
    specific format (RequestFormatModel).
    It base on CRUD.

    Methods:
        * buildCreate(RequestFormatModel): string
        * buildRead(RequestFormatModel): string
        * buildUpdate(RequestFormatModel): string
        * buildDelete(RequestFormatModel): string

    """

    def __init__(self):
        pass

    def buildCreate(self, data):
        """Provide a CREATE request 
        Args: data: RequestFormatModel
        Return: request string
        Exception: RequestFormatModelError data (RequestFormatModel)
        """
        if not isinstance(data, RequestFormatModel):
            raise RequestFormatModelError()

    def buildRead(self, data):
        """Provide a READ request 
        Args: data: RequestFormatModel
        Return: request string
        Exception: RequestFormatModelError data (RequestFormatModel)
        """
        if not isinstance(data, RequestFormatModel):
            raise RequestFormatModelError()

    def buildUpdate(self, data):
        """Provide a UPDATE request 
        Args: data: RequestFormatModel
        Return: request string
        Exception: RequestFormatModelError data (RequestFormatModel)
        """
        if not isinstance(data, RequestFormatModel):
            raise RequestFormatModelError()

    def buildDelete(self, data):
        """Provide a DELETE request 
        Args: data: RequestFormatModel
        Return: request string
        Exception: RequestFormatModelError data (RequestFormatModel)
        """
        if not isinstance(data, RequestFormatModel):
            raise RequestFormatModelError()

class RequestBuilderMySQL(RequestBuilder):
    
    def __init__(self):
        super().__init__()

class RequestBuilderPostgreSQL(RequestBuilder):
    def __init__(self):
        super().__init__()
