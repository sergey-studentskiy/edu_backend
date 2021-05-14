class ContentType:
    VIDEO = 'VIDEO'
    AUDIO = 'AUDIO'
    IMAGE = 'IMAGE'
    TEXT = 'TEXT'

    @classmethod
    def media_content_types(self):
        return [self.AUDIO, self.IMAGE, self.VIDEO]


class ContentTopicStatus:
    IN_PROGRESS = 'IN_PROGRESS'
    ACTIVE = 'ACTIVE'
    SUSPENDED = 'SUSPENDED'


class ContentTopicItemStatus:
    IN_PROGRESS = 'IN_PROGRESS'
    ACTIVE = 'ACTIVE'
    SUSPENDED = 'SUSPENDED'
