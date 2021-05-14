from dtos.base_dto import BaseDTO


class CommentDTO(BaseDTO):
    id: int
    user_name: str
    user_id: int
    content: str
