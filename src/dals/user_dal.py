from typing import List

from common.db.base_dal import BaseDAL
from db.models.user import User
from db.models.user_item import UserItem
from db.models.video_item import VideoItem


class UserDAL(BaseDAL):

    def create_user(self, first_name: str, last_name: str, bob_link: str,
                    user_name: str, password: str) -> User:
        user = User(first_name=first_name, last_name=last_name, bob_link=bob_link, user_name=user_name, password=password)
        self.add_and_flush(user)
        return user

    def get_user(self, user_id: int) -> User:
        return self.db_session.query(User).get(user_id)

    def get_user_by_user_name_and_password(self, user_name: str, password: str):
        return self.db_session.query(User).filter(User.user_name == user_name).filter(User.password == password).one_or_none()

    def get_user_items(self, user_id: int) -> List[VideoItem]:
        return self.db_session.query(VideoItem).join(UserItem).filter(UserItem.user_id == user_id).all()
