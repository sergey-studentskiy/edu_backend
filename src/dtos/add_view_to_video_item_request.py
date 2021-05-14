from dtos.base_dto import BaseDTO


class AddViewToVideoRequest(BaseDTO):
    video_item_id: int
    user_id: int
