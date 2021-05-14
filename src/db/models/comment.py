from sqlalchemy import Column, Integer, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from db.models import Base
from db.models.create_updated_on_fields import CreateUpdateOnFields


class Comment(Base, CreateUpdateOnFields):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey("video_items.id", name="fk_comment_item_id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", name="fk_comment_user_id"), nullable=True)
    user = relationship("User", uselist=False)
    content = Column(Text)
    edited = Column(Boolean, default=False)
    deleted = Column(Boolean, default=False)
