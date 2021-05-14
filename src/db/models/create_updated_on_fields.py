from sqlalchemy import TIMESTAMP, Column, func


class CreateUpdateOnFields:
    last_modified_time = Column(TIMESTAMP, default=func.current_timestamp(), onupdate=func.current_timestamp())
    created_time = Column(TIMESTAMP, default=func.current_timestamp())
