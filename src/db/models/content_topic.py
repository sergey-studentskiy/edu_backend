from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from db.models import Base
from db.models.create_updated_on_fields import CreateUpdateOnFields
from .topic_item import TopicItem
from .video_item import VideoItem


class ContentTopic(Base, CreateUpdateOnFields):
    __tablename__ = 'content_topics'

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    description = Column(Text)
    status = Column(String(100))
    team_id = Column(Integer, ForeignKey("teams.id", name="fk_topic_team"), nullable=True)
