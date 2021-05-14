from db.models.tag import Tag
from dtos.tag_dto import TagDTO


def convert_tag_to_tag_dto(tag: Tag) -> TagDTO:
    return TagDTO(id=tag.id, text=tag.txt)
