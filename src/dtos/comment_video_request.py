from dtos.base_dto import BaseDTO


class CommentVideoRequest(BaseDTO):
    video_item_id: int
    user_id: int
    comment: str
