from common.db.db_session import DBSession
from dals.content_topic_dal import ContentTopicDAL
from helpers.converters.db_model_to_dto.content_topic_converts import convert_content_topic_to_content_topic_dto


class RetrieveAllContentTopics:

    def __init__(self, dal: ContentTopicDAL):
        self._dal = dal

    @DBSession.with_session()
    def retrieve(self):
        content_topics = self._dal.get_all_content_topics()
        return [convert_content_topic_to_content_topic_dto(content_topic) for content_topic in content_topics]

    @classmethod
    def construct(cls):
        return cls(ContentTopicDAL())
