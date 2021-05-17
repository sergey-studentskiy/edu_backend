from sqlalchemy import Column, String, Integer, Text

from db.models import Base
from db.models.create_updated_on_fields import CreateUpdateOnFields


class User(Base, CreateUpdateOnFields):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    bob_link = Column(Text)

    user_name = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
