from typing import Any

from sqlalchemy.orm import Session

from common.db.db_session import DBSession


class BaseDAL:

    @property
    def db_session(self) -> Session:
        return DBSession.get_session()

    def add_and_flush(self, model: Any):
        self.db_session.add(model)
        self.db_session.flush()
