from dals.user_dal import UserDAL


class UserManager:

    def __init__(self, user_dal: UserDAL):
        self._user_dal = user_dal

    def login(self, user_name: str, password: str):
        return self._user_dal.get_user_by_user_name_and_password(user_name, password)

    def create_user(self, first_name: str, last_name: str, bob_link: str,
                    user_name: str, password: str):
        return self._user_dal.create_user(first_name, last_name, bob_link,user_name, password)

    @classmethod
    def construct(cls):
        return cls(UserDAL())
