from bl.tags.tag_manager import TagManager
from common.db.db_session import DBSession
from helpers.converters.db_model_to_dto.tag_converters import convert_tag_to_tag_dto


class CreateTag:

    def __init__(self, tag_mgr: TagManager):
        self._tag_mgr = tag_mgr

    @DBSession.with_session()
    def create(self, txt: str):
        tag = self._tag_mgr.add_tag(txt)
        return convert_tag_to_tag_dto(tag)

    @classmethod
    def construct(cls):
        return cls(TagManager.construct())
