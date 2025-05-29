# app/models.py

from sqlalchemy import Column, Integer, String, DateTime
from .database import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    location = Column(String)
    startDate = Column(DateTime)
    endDate = Column(DateTime)
    url = Column(String)
