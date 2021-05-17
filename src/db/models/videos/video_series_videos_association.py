from sqlalchemy import Column, Integer, ForeignKey, Table

from db.models import Base

VideoSeriesVideosAssociation = Table('video_series_videos_association', Base.metadata,
                                      Column('video_series_id', Integer, ForeignKey('video_series.id')),
                                      Column('video_details_id', Integer, ForeignKey('video_details.id'))
                                      )
