from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

import db.models.users.user
import db.models.comments.comment
import db.models.comments.video_series_comments_association
import db.models.videos.video_details
import db.models.videos.video_series_videos_association
import db.models.videos.video_series
