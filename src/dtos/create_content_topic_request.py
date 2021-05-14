from dtos.base_dto import BaseDTO


class CreateContentTopicRequest(BaseDTO):
    title: str
    description: str
