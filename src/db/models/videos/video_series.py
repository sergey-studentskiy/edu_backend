from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import relationship

from db.models import Base
from db.models.comments.video_series_comments_association import VideoSeriesCommentAssociation
from db.models.create_updated_on_fields import CreateUpdateOnFields
from db.models.videos.video_series_videos_association import VideoSeriesVideosAssociation


class VideoSeries(Base, CreateUpdateOnFields):
    __tablename__ = 'video_series'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(Text)

    comments = relationship("Comment", secondary=VideoSeriesCommentAssociation, back_populates="video_series")
    videos = relationship("Comment", secondary=VideoSeriesVideosAssociation, back_populates="video_series")
