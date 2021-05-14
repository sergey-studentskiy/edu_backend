from sqlalchemy import Column, String, Integer

from db.models import Base
from db.models.create_updated_on_fields import CreateUpdateOnFields


class Team(Base, CreateUpdateOnFields):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
