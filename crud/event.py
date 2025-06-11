from database import events
from models import Event as EventModel
from schemas.event import EventCreate, EventUpdate

class EventCrud:

    @staticmethod
    def create_event(event_data: EventCreate):
        event_id = len(events) + 1
        new_event = EventModel(
            id=event_id,
            title=event_data.title,
            location=event_data.location,
            date=event_data.date,
            is_open=True
        )
        events.append(new_event)
        return new_event
    
    @staticmethod
    def get_all_events():
        return events
    
    @staticmethod
    def get_event_by_id(event_id:int):
        for event in events:
            if event.id == event_id:
                return event
        return None
    
    @staticmethod
    def update_event(event_id: int, event_data: EventUpdate):
        event = event_crud.get_event_by_id(event_id)
        if event:
            event.title = event_data.title
            event.location = event_data.location
            event.date = event_data.date
            return event
        return None
    
    @staticmethod
    def delete_event(event_id: int):
        event = event_crud.get_event_by_id(event_id)
        if event:
            events.remove(event)
            return True
        return False
    
    @staticmethod
    def close_event(event_id: int):
        event = event_crud.get_event_by_id(event_id)
        if event:
            event.is_open = not event.is_open
            return event
        return None
    
event_crud = EventCrud()
