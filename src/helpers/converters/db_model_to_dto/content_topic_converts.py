from db.models.content_topic import ContentTopic
from dtos.content_topic_dto import ContentTopicDTO


def convert_content_topic_to_content_topic_dto(db_model: ContentTopic) -> ContentTopicDTO:
    return ContentTopicDTO(id=db_model.id, title=db_model.title, description=db_model.description, status=db_model.status)
