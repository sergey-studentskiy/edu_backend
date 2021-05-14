from bl.video_item.video_item_manager import VideoItemManager
from common.db.db_session import DBSession
from helpers.converters.db_model_to_dto.video_converters import convert_video_item_to_video_item_dto


class GetNewestVideoItems:

    def __init__(self, video_item_mgr: VideoItemManager):
        self._video_item_mgr = video_item_mgr

    @DBSession.with_session()
    def get(self):
        videos = self._video_item_mgr.get_newest_video_items()
        return [convert_video_item_to_video_item_dto(video) for video in videos]

    @classmethod
    def construct(cls):
        return cls(VideoItemManager.construct())
