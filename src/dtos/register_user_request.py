from typing import Optional

from dtos.base_dto import BaseDTO


class RegisterUserRequest(BaseDTO):
    first_name: str
    last_name: str
    user_name: str
    password: str

    bob_link: Optional[str] = None
