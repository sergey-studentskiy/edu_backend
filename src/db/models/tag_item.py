from sqlalchemy import Column, Integer, ForeignKey

from db.models import Base
from db.models.create_updated_on_fields import CreateUpdateOnFields


class TagItem(Base, CreateUpdateOnFields):
    __tablename__ = 'tag_items'

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey("video_items.id", name="fk_tag_item"), nullable=True)
    tag_id = Column(Integer, ForeignKey("tags.id", name="fk_item_tag"), nullable=True)
