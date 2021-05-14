from common.db.db_session import DBSession

from dals.content_topic_dal import ContentTopicDAL
from helpers.converters.db_model_to_dto.content_topic_converts import convert_content_topic_to_content_topic_dto


class DeleteContentTopic:

    def __init__(self, dal: ContentTopicDAL):
        self._dal = dal

    @DBSession.with_session()
    def create_content_topic(self, id: int, title: str, description: str, status: str):
        content_topic = self._dal.get_content_topic_by_id(id)
        content_topic.status = status
        content_topic.title = title
        content_topic.description = description
        return convert_content_topic_to_content_topic_dto(content_topic)
