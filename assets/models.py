from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, Text
from assets.database import Base


class Data(Base):
    __tablename__ = "data"
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=False)
    article = Column(Text, unique=False)
    timestamp = Column(DateTime, unique=False)

    def __init__(self, name=None, article=None, timestamp=None):
        self.name = name
        self.article = article
        self.timestamp = timestamp
