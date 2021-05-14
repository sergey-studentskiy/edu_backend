from dals.tag_dal import TagDAL


class TagManager:

    def __init__(self, tag_dal: TagDAL):
        self._tag_dal = tag_dal

    def add_tag(self, text: str):
        return self._tag_dal.add_tag(text)

    def get_all(self):
        return self._tag_dal.get_all_tags()

    @classmethod
    def construct(cls):
        return cls(TagDAL())
