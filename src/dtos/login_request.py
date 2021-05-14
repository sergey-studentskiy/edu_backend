from dtos.base_dto import BaseDTO


class LoginRequest(BaseDTO):
    user_name: str
    password: str
