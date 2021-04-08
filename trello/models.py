from sqlalchemy import Column, Integer, String

from trello.db.base import Base


class Board(Base):
    __tablename__ = "boards"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String, unique=True)
    description = Column(String, nullable=True)
