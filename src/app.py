import uvicorn
from fastapi import FastAPI, Form, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from bl.comments.add_comment import AddComment
from bl.tags.create_tag import CreateTag
from bl.tags.retrieve_all_tags import RetrieveAllTags
from bl.users.login import Login
from bl.users.register_user import RegisterUser
from bl.video_item.create_video_item import CreateVideoItem
from bl.video_item.get_newest_video_items import GetNewestVideoItems
from bl.video_item.get_video_item import GetVideoItem
from bl.video_item.search_engine_manager import SearchEngineManager
from bl.video_item.vlc_manager import VLCManager
from dtos.add_view_to_video_item_request import AddViewToVideoRequest
from dtos.comment_video_request import CommentVideoRequest
from dtos.create_tag_request import CreateTagRequest
from dtos.like_unlike_video_request import LikeUnlikeVideoRequest
from dtos.login_request import LoginRequest
from dtos.register_user_request import RegisterUserRequest

origins = ["*"]
app = FastAPI()
app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)


# region Video endpoints


@app.get("/video_items/newest")
def get_newest_video_items():
    bp = GetNewestVideoItems.construct()
    return bp.get()


@app.post("/video_item/create")
def video_item(title: str = Form(...),
               file: UploadFile = File(...),
               description: str = Form(...)):
    bp = CreateVideoItem.construct()
    return bp.create(title, file, description)


@app.get("/video_item/{video_id}")
def get_video_item(video_id: int):
    bp = GetVideoItem.construct()
    return bp.get(video_id)


@app.get("/search/{phrase}")
def search_videos(phrase: str):
    manager = SearchEngineManager.construct()
    return manager.search_video_by_phrase(phrase)


# endregion Video endpoints

# region User endpoints

@app.post("/user/register")
def register_user(register_user: RegisterUserRequest):
    bp = RegisterUser.construct()
    return bp.register(register_user)


@app.post("/user/login")
def login_user(login_user: LoginRequest):
    bp = Login.construct()
    return bp.get(login_user)


# endregion User endpoints

# region Tag endpoints
@app.post("/tag/create")
def create_tag(tag: CreateTagRequest):
    bp = CreateTag.construct()
    return bp.create(tag.text)


@app.get("/tags/all")
def create_tag():
    bp = RetrieveAllTags.construct()
    return bp.get()


# endregion Tag endpoints

# region View/Like/Comment endpoints

@app.post("/video_item/commment")
def comment_video_item(comment: CommentVideoRequest):
    bp = AddComment.construct()
    return bp.add(comment)


@app.post("/video_item/view")
def add_view_to_video_item(view: AddViewToVideoRequest):
    manager = VLCManager.construct()
    manager.view_video_item(view)


@app.post("/video_item/user_like")
def like_video_item(like: LikeUnlikeVideoRequest):
    manager = VLCManager.construct()
    manager.like_video_item(like)


@app.post("/video_item/user_unlike")
def unlike_video_item(unlike: LikeUnlikeVideoRequest):
    manager = VLCManager.construct()
    manager.unlike_video_item(unlike)


# endregionView/Like/Comments endpoints

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
