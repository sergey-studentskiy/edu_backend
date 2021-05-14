from typing import Optional, List

from dtos.base_dto import BaseDTO
from dtos.comment_dto import CommentDTO


class VideoItemDTO(BaseDTO):
    id: int
    title: str
    description: str
    thumbnail_url: str
    video_url: str
    likes: int
    views: int
    comments: Optional[List[Optional[CommentDTO]]] = None
