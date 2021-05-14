from typing import Optional

from dtos.base_dto import BaseDTO


class ContentTopicItemDTO(BaseDTO):
    title: str
    order: int
    source_url: Optional[str]
    text_content: Optional[str]
    content_type: str
    status: str

    id: Optional[int] = None
