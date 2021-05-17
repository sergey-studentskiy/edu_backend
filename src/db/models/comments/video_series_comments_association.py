from sqlalchemy import Column, Integer, ForeignKey, Table

from db.models import Base

VideoSeriesCommentAssociation = Table('video_series_comment_association', Base.metadata,
                                      Column('video_series_id', Integer, ForeignKey('video_series.id')),
                                      Column('comment_id', Integer, ForeignKey('comments.id'))
                                      )
