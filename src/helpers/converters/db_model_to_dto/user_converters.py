from db.models.user import User
from dtos.login_response import LoginResponse


def convert_user_to_login_response(db_model: User) -> LoginResponse:
    return LoginResponse(id=db_model.id, user_name=db_model.user_name)
