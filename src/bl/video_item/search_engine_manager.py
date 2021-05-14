from typing import List

from common.db.db_session import DBSession
from dals.video_item_dal import VideoItemDal
from dtos.video_item_dto import VideoItemDTO
from helpers.converters.db_model_to_dto.video_converters import convert_video_item_to_video_item_dto


class SearchEngineManager:
    def __init__(self, video_item_dal):
        self.video_item_dal: VideoItemDal = video_item_dal

    @classmethod
    def construct(cls):
        dal = VideoItemDal()
        return cls(dal)

    @DBSession.with_session()
    def search_video_by_phrase(self, phrase: str) -> List[VideoItemDTO]:
        results = self.video_item_dal.search_video_by_phrase(phrase)
        return [convert_video_item_to_video_item_dto(video) for video in results]
