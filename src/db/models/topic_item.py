from sqlalchemy import Column, Integer, ForeignKey

from db.models import Base
from db.models.create_updated_on_fields import CreateUpdateOnFields


class TopicItem(Base, CreateUpdateOnFields):
    __tablename__ = 'topic_items'

    id = Column(Integer, primary_key=True)
    topic_id = Column(Integer, ForeignKey("content_topics.id", name="fk_content_topic_id"), nullable=True)
    item_id = Column(Integer, ForeignKey("video_items.id", name="fk_topic_item_id"), nullable=True)
    topic_order = Column(Integer)
