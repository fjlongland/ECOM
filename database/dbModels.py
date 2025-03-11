from .database import Base
from sqlalchemy import Column, String, Integer

class Test(Base):
    __tablename__="test"

    test_int = Column(Integer, primary_key=True, nullable=False)
    test_str = Column(String, nullable=False)