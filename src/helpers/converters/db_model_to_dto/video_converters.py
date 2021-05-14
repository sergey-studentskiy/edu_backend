from db.models.comment import Comment
from db.models.video_item import VideoItem
from dtos.comment_dto import CommentDTO
from dtos.video_item_dto import VideoItemDTO


def convert_video_item_to_video_item_dto(db_model: VideoItem) -> VideoItemDTO:
    return VideoItemDTO(id=db_model.id, title=db_model.title, description=db_model.description,
                        thumbnail_url=db_model.thumbnail_url, video_url=db_model.source_url,
                        comments= [] or[convert_comment_to_comment_dto(comment) for comment in db_model.comments],
                        likes=len(db_model.likes),
                        views=len(db_model.views))


def convert_comment_to_comment_dto(comment: Comment) -> CommentDTO:
    return CommentDTO(id=comment.id,
                      user_id=comment.user_id,
                      user_name=comment.user.user_name,
                      content=comment.content)
