from rest_framework.response import Response
from rest_framework import status


class CustomResponse:
    def __init__(self, message=None, data=None, headers=None):
        self.message = message
        self.data = data
        self.headers = headers

    def success(self, status_code=status.HTTP_200_OK):
        if status_code < 200 or status_code > 226:
            raise ValueError("Invalid HTTP status code.")
        return Response(
            {"message": self.message, "data": self.data},
            status_code,
            headers=self.headers,
        )

    def errors(self, status_code=status.HTTP_400_BAD_REQUEST):
        if isinstance(self.data, str):
            self.data = [self.data]
        if status_code < 400 or status_code > 521:
            raise ValueError("Invalid HTTP status code.")
        return Response(
            {"message": self.message, "errors": self.data},
            status_code,
            headers=self.headers,
        )