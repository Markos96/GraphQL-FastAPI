from sqlalchemy import Column, String, Integer
from app.config.db import Base
from sqlalchemy.orm import relationship


class League(Base):
    __tablename__ = "league"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(100), nullable=False)
    teams = relationship("Team", back_populates="league")
