from sqlalchemy import Column, Integer, ForeignKey, Boolean, UniqueConstraint

from db.models import Base
from db.models.create_updated_on_fields import CreateUpdateOnFields


class Like(Base, CreateUpdateOnFields):
    __tablename__ = 'likes'

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey("video_items.id", name="fk_like_item"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", name="fk_like_user"), nullable=True)
    like = Column(Boolean)

    UniqueConstraint('item_id', 'user_id', name='video_user_like')
