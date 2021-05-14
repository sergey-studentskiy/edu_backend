from common.db.db_session import DBSession
from common.exceptions.content_topic_exceptions import VideoNotFound, UserNotFound
from dals.user_dal import UserDAL
from dals.video_item_dal import VideoItemDal
from dals.vlc_dal import VlcDAL
from db.models.user import User
from db.models.video_item import VideoItem
from dtos.add_view_to_video_item_request import AddViewToVideoRequest
from dtos.like_unlike_video_request import LikeUnlikeVideoRequest


class VLCManager:
    def __init__(self, vlc_dal: VlcDAL, user_dal: UserDAL, video_item_dal: VideoItemDal):
        self.vlc_dal = vlc_dal
        self.user_dal = user_dal
        self.video_item_dal = video_item_dal

    @classmethod
    def construct(cls):
        vlc_dal = VlcDAL()
        user_dal = UserDAL()
        video_item_dal = VideoItemDal()
        return cls(vlc_dal, user_dal, video_item_dal)

    @DBSession.with_session()
    def like_video_item(self, like: LikeUnlikeVideoRequest):
        video_item = self.verify_video(like.video_item_id)
        user = self.verify_user(like.user_id)
        like = self.vlc_dal.get_like_object(like.video_item_id, like.user_id)
        if not like:
            self.vlc_dal.like_video_item(video_item=video_item, user=user)
        else:
            like.like = True

    @DBSession.with_session()
    def unlike_video_item(self, unlike: LikeUnlikeVideoRequest):
        like = self.vlc_dal.get_like_object(unlike.video_item_id, unlike.user_id)
        if like:
            self.vlc_dal.delete_like_object(like.id)

    @DBSession.with_session()
    def view_video_item(self, view: AddViewToVideoRequest):
        video_item = self.verify_video(view.video_item_id)
        user = self.verify_user(view.user_id)
        self.vlc_dal.add_view_to_video_item(video_item, user)

    def verify_video(self, video_item_id) -> VideoItem:
        video = self.video_item_dal.get_video_by_id(video_item_id)
        if not video: raise VideoNotFound()
        return video

    def verify_user(self, user_id) -> User:
        user = self.user_dal.get_user(user_id)
        if not user: raise UserNotFound()
        return user

    def comment_on_video(self, video_id: int, user_id: int, content: str):
        return self.vlc_dal.comment_on_video(video_id, user_id, content)

    @DBSession.with_session()
    def edit_comment(self, comment_id: int, content: str):
        comment = self.vlc_dal.get_comment(comment_id)
        comment.content = content
        return comment
