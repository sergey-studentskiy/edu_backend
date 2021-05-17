from sqlalchemy import Column, String, Integer

from db.models import Base
from db.models.create_updated_on_fields import CreateUpdateOnFields


class VideoDetails(Base, CreateUpdateOnFields):
    __tablename__ = 'video_details'

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    source_url = Column(String(1200))
    thumbnail_url = Column(String(1200))
