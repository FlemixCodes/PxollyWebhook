class VkError(Exception):
    ...


class VkResponseError(Exception):
    def __init__(self, error_code, error_msg) -> None:
        self.error_code = error_code
        self.error_msg = error_msg

    def __str__(self) -> str:
        return f"({self.error_code}) {self.error_msg}"


class ResponseError(Exception):
    pass
