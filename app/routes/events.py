# app/routes/events.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import SessionLocal
from datetime import timezone

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/events", response_model=list[schemas.Event])
def read_events(db: Session = Depends(get_db)):
    events = crud.get_events(db)

    for event in events:
        if event.startDate.tzinfo is None:
            event.startDate = event.startDate.replace(tzinfo=timezone.utc)
        if event.endDate.tzinfo is None:
            event.endDate = event.endDate.replace(tzinfo=timezone.utc)
    return events
