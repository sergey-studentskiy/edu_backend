from typing import List, Optional

from common.db.base_dal import BaseDAL
from db.models.playlist import Playlist
from db.models.playlist_item import PlaylistItem
from db.models.video_item import VideoItem


class PlaylistDAL(BaseDAL):

    def create_playlist(self, name: str, item_id_list: Optional[List[int]] = None) -> Playlist:
        playlist = Playlist(name=name)
        self.add_and_flush(playlist)
        return playlist

    def add_item_to_playlist(self, playlist_id: int, item_id: int) -> int:
        pl_item = PlaylistItem(playlist_id, item_id)
        self.add_and_flush(pl_item)
        return pl_item.id

    def get_playlist(self, playlist_id: int) -> Playlist:
        return self.db_session.query(Playlist).get(playlist_id)

    def get_playlist_items(self, playlist_id: int) -> List[VideoItem]:
        return self.db_session.query(VideoItem).join(PlaylistItem).filter(PlaylistItem.playlist_id == playlist_id).all()
