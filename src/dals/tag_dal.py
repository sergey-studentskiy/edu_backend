from common.db.base_dal import BaseDAL
from db.models.tag import Tag


class TagDAL(BaseDAL):

    def add_tag(self, text: str) -> Tag:
        tag = Tag(txt=text)
        self.add_and_flush(tag)
        return tag

    def get_all_tags(self):
        return self.db_session.query(Tag).all()
