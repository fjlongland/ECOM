from .database import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

class Test(Base):
    __tablename__="test"

    test_int = Column(Integer, primary_key=True, nullable=False)
    test_str = Column(String, nullable=False)


class User(Base):
    __tablename__="user"

    user_id = Column(Integer, primary_key=True, nullable=False)
    user_name = Column(String, nullable=False)
    user_password = Column(String, nullable=False)
    date_created = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

