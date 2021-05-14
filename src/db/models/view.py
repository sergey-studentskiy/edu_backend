from sqlalchemy import Column, Integer, ForeignKey, Boolean

from db.models import Base
from db.models.create_updated_on_fields import CreateUpdateOnFields


class View(Base, CreateUpdateOnFields):
    __tablename__ = 'views'

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey("video_items.id", name="fk_view_item"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", name="fk_view_user"), nullable=True)
    seconds_in_video = Column(Integer, nullable=True)
