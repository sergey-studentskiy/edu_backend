from sqlalchemy import Column, String, Integer

from db.models import Base
from db.models.create_updated_on_fields import CreateUpdateOnFields


class Playlist(Base, CreateUpdateOnFields):
    __tablename__ = 'playlists'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
