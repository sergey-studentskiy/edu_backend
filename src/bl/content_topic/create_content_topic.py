from common.consts.content_consts import ContentTopicStatus
from common.db.db_session import DBSession
from dals.content_topic_dal import ContentTopicDAL
from dtos.create_content_topic_request import CreateContentTopicRequest
from helpers.converters.db_model_to_dto.content_topic_converts import convert_content_topic_to_content_topic_dto


class CreateContentTopic:

    def __init__(self, dal: ContentTopicDAL):
        self._dal = dal

    @DBSession.with_session()
    def create(self, request: CreateContentTopicRequest):
        content_topic = self._dal.create_content_topic(request.title, request.description, ContentTopicStatus.IN_PROGRESS)
        return convert_content_topic_to_content_topic_dto(content_topic)

    @classmethod
    def construct(cls):
        return cls(ContentTopicDAL())
