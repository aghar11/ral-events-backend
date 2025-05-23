# app/main.py

from fastapi import FastAPI
from .routes import events
from .database import Base, engine

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Mount the router
app.include_router(events.router)
