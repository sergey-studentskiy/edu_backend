from sqlalchemy import Column, String, Integer

from db.models import Base
from db.models.create_updated_on_fields import CreateUpdateOnFields


class Tag(Base, CreateUpdateOnFields):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    txt = Column(String(250))
