from bl.video_item.vlc_manager import VLCManager
from common.db.db_session import DBSession
from dtos.comment_video_request import CommentVideoRequest
from helpers.converters.db_model_to_dto.video_converters import convert_comment_to_comment_dto


class AddComment:

    def __init__(self, vlc_mgr: VLCManager):
        self._vls_mgr = vlc_mgr

    @DBSession.with_session()
    def add(self, comment_on_video: CommentVideoRequest):
        comment = self._vls_mgr.comment_on_video(comment_on_video.video_item_id, comment_on_video.user_id, comment_on_video.comment)
        return convert_comment_to_comment_dto(comment)

    @classmethod
    def construct(cls):
        return cls(VLCManager.construct())
