from bl.users.user_manager import UserManager
from common.db.db_session import DBSession
from dtos.register_user_request import RegisterUserRequest
from helpers.converters.db_model_to_dto.user_converters import convert_user_to_login_response


class RegisterUser:

    def __init__(self, user_mgr: UserManager):
        self._user_mgr = user_mgr

    @DBSession.with_session()
    def register(self, register_user: RegisterUserRequest):
        user = self._user_mgr.create_user(register_user.first_name, register_user.last_name,
                                          register_user.bob_link, register_user.user_name, register_user.password)
        return convert_user_to_login_response(user)

    @classmethod
    def construct(cls):
        return cls(UserManager.construct())
