from dataclasses import asdict, dataclass

from common.db.db_session import DBSession
from dals.video_item_dal import VideoItemDal
from db.models.video_item import VideoItem


@dataclass
class VideoItemResponse:
    title: str
    description: str
    source_url: str
    likes_counter: int
    views_counter: int



class VideoItemManager:
    def __init__(self, video_item_dal):
        self.video_item_dal = video_item_dal

    @classmethod
    def construct(cls):
        dal = VideoItemDal()
        return cls(dal)

    def add_video(self,  title: str, video_url: str, thumbnail_url: str, description: str) -> VideoItem:
        video = self.video_item_dal.add_video( title, video_url, thumbnail_url, description)
        return video

    def get_newest_video_items(self):
        return self.video_item_dal.get_newest_video_items()

    def get_video_item_by_id(self, video_item_id: int):
        return self.video_item_dal.get_video_by_id(video_item_id)

    @DBSession.with_session()
    def get_search_list(self, search: str):
        return self.video_item_dal.get_list_of_video_by_prefix(search)

    @DBSession.with_session()
    def get_video_details(self, video_item_id: int):
        video: VideoItem = self.video_item_dal.get_video_by_id(video_item_id)
        video_item_response = VideoItemResponse(video.title, video.description, video.source_url, video.likes_count, video.views_count)
        return asdict(video_item_response)

    @DBSession.with_session()
    def remove_by_id(self, video_id: int):
        self.video_item_dal.delete_by_id(video_id)
