from common.consts.content_consts import ContentTopicStatus
from common.db.base_dal import BaseDAL
from db.models.content_topic import ContentTopic


class ContentTopicDAL(BaseDAL):

    def create_content_topic(self, title: str, description: str, status: str):
        content_topic = ContentTopic(title=title, description=description, status=status)
        self.add_and_flush(content_topic)
        return content_topic

    def get_content_topic_by_id(self, topic_id: int) -> ContentTopic:
        return self.db_session.query(ContentTopic).get(topic_id)

    def delete_content_topic(self, topic_id):
        self.db_session.query(ContentTopic).filter(ContentTopic.id == topic_id).delete()

    def get_all_content_topics(self):
        return self.db_session.query(ContentTopic).filter(ContentTopic.status == ContentTopicStatus.ACTIVE).all()
