from typing import List

from sqlalchemy import or_
from sqlalchemy.dialects import mysql

from common.db.base_dal import BaseDAL
from db.models.user import User
from db.models.user_item import UserItem
from db.models.video_item import VideoItem

NUM_OF_SEARCH_RESULTS = 5


class VideoItemDal(BaseDAL):

    def get_video_by_id(self, id: int) -> VideoItem:
        return self.db_session.query(VideoItem).get(id)

    def get_newest_video_items(self):
        return self.db_session.query(VideoItem).order_by(VideoItem.created_time.desc()).all()

    def get_list_of_video_by_prefix(self, prefix: str) -> List[VideoItem]:
        search = "{}%".format(prefix)
        return self.db_session.query(VideoItem).filter(VideoItem.title.like(search)).limit(NUM_OF_SEARCH_RESULTS).all()

    def get_video_by_name(self, name: str) -> List[VideoItem]:
        return self.db_session.query(VideoItem).filter(VideoItem.title == name).all()

    def add_video(self, title: str, video_url: str, thumbnail_url: str, description: str) -> VideoItem:
        video = VideoItem(title=title, source_url=video_url, thumbnail_url=thumbnail_url,
                          description=description)
        self.add_and_flush(video)
        return video

    def delete_by_id(self, video_id):
        self.db_session.query(VideoItem).get(video_id).delete()

    def search_video_by_phrase(self, text_phrase: str):
        q = self.db_session.query(VideoItem).join(UserItem, UserItem.item_id == VideoItem.id, isouter=True). \
            join(User, UserItem.user_id == User.id).filter(
                or_(
                        VideoItem.title.contains(text_phrase),
                        VideoItem.description.contains(text_phrase),
                        User.first_name.contains(text_phrase),
                        User.last_name.contains(text_phrase)
                )
        )

        return q.all()
