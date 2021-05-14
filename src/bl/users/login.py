from bl.users.user_manager import UserManager
from common.db.db_session import DBSession
from common.exceptions.user_exceptions import UserNotFoundException
from dtos.login_request import LoginRequest
from helpers.converters.db_model_to_dto.user_converters import convert_user_to_login_response


class Login:

    def __init__(self, user_mgr: UserManager):
        self._user_mgr = user_mgr

    @DBSession.with_session()
    def get(self, login: LoginRequest):
        user = self._user_mgr.login(login.user_name, login.password)
        if not user:
            raise UserNotFoundException()
        return convert_user_to_login_response(user)

    @classmethod
    def construct(cls):
        return cls(UserManager.construct())
