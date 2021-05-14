from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import relationship

from db.models import Base
from db.models.create_updated_on_fields import CreateUpdateOnFields


class VideoItem(Base, CreateUpdateOnFields):
    __tablename__ = 'video_items'

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    source_url = Column(String(1200))
    description = Column(Text)
    thumbnail_url = Column(String(1200))

    comments = relationship('Comment', backref='video_item')
    likes = relationship('Like', backref='video_item')
    views = relationship('View', backref='video_item')

