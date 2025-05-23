# app/crud.py

from sqlalchemy.orm import Session
from . import models, schemas

def get_events(db: Session):
    return db.query(models.Event).all()

def get_events_by_date(db: Session, date: str):
    return db.query(models.Event).filter(models.Event.startDate.cast(Date) == date).all()
