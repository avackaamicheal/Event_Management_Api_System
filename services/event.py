# app/services/event.py
from crud.event import event_crud as crud
from models import Event
from datetime import date
from schemas.event import EventUpdate, EventCreate


class EventService:
    @staticmethod
    def create_event_service(title: str, location: str, date: date):
        """Business logic for creating an event"""
        # Validate title length
        if len(title) < 5:
            raise ValueError("Event title must be at least 5 characters")
        
        if date <= date.today():
            raise ValueError("Event date must be in the future")
        
        return crud.create_event(
            EventCreate(title=title, location=location, date=date)
        )
    

    @staticmethod
    def update_event_service(event_id: int, update_data: EventUpdate):
        """Business logic for updating an event"""
        # Additional validations can be added here
        if "date" in update_data:
            from datetime import date 
            if update_data["date"] <= date.today():
                raise ValueError("Event date must be in the future")
        
        return crud.update_event(event_id, update_data)
    
    @staticmethod
    def close_event_service(event_id: int):
        """Business logic for closing event registration"""
        event = crud.get_event_by_id(event_id)
        if not event:
            return None
        
        return crud.close_event(event_id)
    
    @staticmethod
    def get_upcoming_events_service():
        """Get all upcoming events"""
        from datetime import date
        events = crud.get_all_events()
        return [e for e in events if e.date > date.today()]
    

event_service = EventService()