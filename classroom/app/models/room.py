from sqlalchemy import Column, Integer, String

from app.models.base import Base


class Room(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未名')
    number = Column(Integer())
    abstract = Column(String(1000))
    image = Column(String(200))
    classify = Column(String(20))
    video = Column(String(200))

