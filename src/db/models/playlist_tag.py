from sqlalchemy import Column, Integer, ForeignKey

from db.models import Base
from db.models.create_updated_on_fields import CreateUpdateOnFields


class PlaylistItem(Base, CreateUpdateOnFields):
    __tablename__ = 'playlist_items'

    id = Column(Integer, primary_key=True)
    playlist_id = Column(Integer, ForeignKey("playlists.id", name="fk_playlist_tag"), nullable=True)
    tag_id = Column(Integer, ForeignKey("tags.id", name="fk_tag_playlist"), nullable=True)
