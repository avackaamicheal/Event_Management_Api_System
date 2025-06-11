# schemas/event.py

from pydantic import BaseModel
from datetime import date
from typing import Optional


class EventBase(BaseModel):
    title: str
    location: str
    date: date

class EventCreate(EventBase):
    pass
    is_open: bool = True


class EventUpdate(EventBase):
    title: Optional[str]= None
    location: Optional[str] = None
    date: Optional[date]

class Event(EventCreate):
    id: int
    