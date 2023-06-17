from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.config.db import Base


class Team(Base):
    __tablename__ = "team"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(100), nullable=False)
    stadium = Column(String(100), nullable=False)
    nickname = Column(String(100), nullable=False)
    id_league = Column(Integer, ForeignKey('league.id'))

    league = relationship("League", back_populates="teams")
    players = relationship("Player", back_populates="team")

