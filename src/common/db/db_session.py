from functools import wraps
from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


class DBSession:
    OPEN_SESSION = {}

    def __init__(self):
        self._session: Optional[Session] = None
        self._engine = create_engine('mysql+pymysql://root:ByXAHoxEuEskT^7cDsuaxmt6@localhost:3306/fbx_education', echo=True)

    def __enter__(self):
        session_cls = sessionmaker(bind=self._engine)
        self._session = session_cls()
        DBSession.OPEN_SESSION[self.__class__.__name__] = self._session
        return self._session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not exc_type:
            self._session.commit()
        else:
            self._session.rollback()

        self._session = None

    @classmethod
    def get_session(cls):
        if not DBSession.OPEN_SESSION.get(cls.__name__):
            raise Exception('There is no open session')
        return DBSession.OPEN_SESSION.get(cls.__name__)

    @classmethod
    def with_session(db_session_class):
        """
            :param Class - the class of the db session (for example - PaymentsDBSession)
            A decorator that will open  a context manager of the specified db session before entering the underlying
            function, end close it after the function finishes
        """

        def underlying(fn):
            @wraps(fn)
            def inner(self, *args, **kwargs):
                with db_session_class() as _:
                    return fn(self, *args, **kwargs)

            return inner

        return underlying
