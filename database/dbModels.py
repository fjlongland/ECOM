from .database import Base
from sqlalchemy import Column, String, Integer, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text


#here we define and create all the database tables.

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

class Post(Base):
    __tablename__="post"

    post_id = Column(Integer, primary_key=True, nullable=False)
    post_title = Column(String, nullable=False)
    post_content = Column(String, nullable=False)
    user_id_fk = Column(Integer, ForeignKey("user.user_id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    date_created = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))

    owner = relationship("User")

class Image(Base):
    __tablename__ = "image"

    image_id = Column(Integer, primary_key=True, nullable=False)
    image_loc = Column(String, nullable=False)
    post_id_fk = Column(Integer, ForeignKey("post.post_id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)

    owner = relationship("Post")