import cv2
from fastapi import UploadFile

from bl.video_item.video_item_manager import VideoItemManager
from common.db.db_session import DBSession
from helpers.converters.db_model_to_dto.video_converters import convert_video_item_to_video_item_dto
from helpers.s3_helper.s3_client import S3Client
import os


class CreateVideoItem:

    def __init__(self, video_item_mgr: VideoItemManager,
                 s3_client: S3Client):
        self._video_item_mgr = video_item_mgr
        self._s3_client = s3_client

    @DBSession.with_session()
    def create(self,
               title: str,
               file: UploadFile,
               description: str):
        video_url = self._s3_client.upload_file_to_bucket(file.file, file.filename)
        thumbnail_url = self._create_thumbnail(file.filename, video_url)
        os.remove("image.jpg")
        new_video_item = self._video_item_mgr.add_video(title, video_url, thumbnail_url, description)
        return convert_video_item_to_video_item_dto(new_video_item)

    def _create_thumbnail(self, file_name: str, url: str):
        extension_start_index = file_name.rfind(".")
        file_name_no_ext = file_name[0:extension_start_index]
        vidcap = cv2.VideoCapture(url)
        vidcap.set(cv2.CAP_PROP_POS_MSEC, 0.5 * 1000)
        hasFrames, image = vidcap.read()
        if hasFrames:
            cv2.imwrite("image.jpg", image)
            return self._s3_client.upload_file_name_to_bucket("image.jpg", file_name_no_ext + ".jpg")

    @classmethod
    def construct(cls):
        return cls(VideoItemManager.construct(), S3Client())
