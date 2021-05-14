from typing import List, Optional

from common.db.base_dal import BaseDAL
from db.models.comment import Comment
from db.models.like import Like
from db.models.user import User
from db.models.video_item import VideoItem
from db.models.view import View


class VlcDAL(BaseDAL):

    def like_video_item(self, video_item: VideoItem, user: User) -> int:
        like = Like(item_id=video_item.id, user_id=user.id, like=True)
        self.add_and_flush(like)
        return self.db_session.query(Like).filter(Like.item_id == video_item.id).filter(Like.like == True).count()

    def add_view_to_video_item(self, video_item: VideoItem, user: User) -> View:
        view = View(item_id=video_item.id, user_id=user.id)
        return view

    def delete_like_object(self, item_id: int) -> None:
        like_object = self.db_session.query(Like).get(item_id)
        self.db_session.delete(like_object)

    def comment_on_video(self, video_id: int, user_id: int, content: str) -> Comment:
        comment = Comment(item_id=video_id, user_id=user_id, content=content, edited=False)
        self.add_and_flush(comment)
        return comment

    def get_comment(self, comment_id: int):
        return self.db_session.query(Comment).get(comment_id)

    def get_item_comments(self, item_id: int) -> List[Comment]:
        return self.db_session.query(Comment).filter(Comment.item_id == item_id).filter(Comment.deleted == False).all()

    def get_like_object(self, item_id: int, user_id: int) -> Optional[Like]:
        return self.db_session.query(Like).filter(Like.item_id == item_id).filter(Like.user_id == user_id).one_or_none()

    def get_video_views_count(self, item_id: int) -> int:
        return self.db_session.query(View).filter(View.item_id == item_id).distinct(View.user_id).count()
