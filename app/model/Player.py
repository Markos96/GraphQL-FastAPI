from sqlalchemy import Column, String, Integer, ForeignKey
from app.config.db import Base
from sqlalchemy.orm import relationship


class Player(Base):
    __tablename__ = "player"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    number = Column(Integer, nullable=False)
    id_team = Column(Integer, ForeignKey('team.id'))

    team = relationship("Team", back_populates="players")
