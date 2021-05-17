from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from db.models import Base
from db.models.create_updated_on_fields import CreateUpdateOnFields
from db.models.users.user import User
from db.models.videos.video_details import VideoItem


class UserItem(Base, CreateUpdateOnFields):
    __tablename__ = 'user_items'

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey("video_items.id", name="fk_item_user"), nullable=True)
    user_id = Column(Integer, ForeignKey("users.id", name="fk_user_item"), nullable=True)

    user = relationship(User, foreign_keys=[user_id])
    item = relationship(VideoItem, foreign_keys=[item_id])
