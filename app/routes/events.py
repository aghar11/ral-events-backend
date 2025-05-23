# app/routes/events.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/events", response_model=list[schemas.Event])
def read_events(db: Session = Depends(get_db)):
    return crud.get_events(db)
