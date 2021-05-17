from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from db.models import Base
from db.models.create_updated_on_fields import CreateUpdateOnFields


class SingleVideo(Base, CreateUpdateOnFields):
    __tablename__ = 'single_videos'
    video_details_id = Column(Integer, ForeignKey("video_details.id", name="fk_single_video_video_details_id"), nullable=True)
    video_details = relationship("VideoDetails", uselist=False)
