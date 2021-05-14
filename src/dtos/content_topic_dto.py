from dtos.base_dto import BaseDTO


class ContentTopicDTO(BaseDTO):
    title: str
    description: str
    status: str
    id: int
