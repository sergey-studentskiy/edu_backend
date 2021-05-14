from sqlalchemy import Column, Integer, ForeignKey

from db.models import Base
from db.models.create_updated_on_fields import CreateUpdateOnFields


class PlaylistItem(Base, CreateUpdateOnFields):
    __tablename__ = 'playlist_items'

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey("video_items.id", name="fk_playlist_item"), nullable=True)
    playlist_id = Column(Integer, ForeignKey("playlists.id", name="fk_item_playlist"), nullable=True)
