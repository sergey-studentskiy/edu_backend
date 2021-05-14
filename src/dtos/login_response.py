from dtos.base_dto import BaseDTO


class LoginResponse(BaseDTO):
    id: int
    user_name: str
