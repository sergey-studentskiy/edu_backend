from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

import db.models.comment
import db.models.content_topic
import db.models.like
import db.models.tag
import db.models.tag_item
import db.models.team
import db.models.topic_item
import db.models.user
import db.models.user_item
import db.models.video_item
import db.models.view
