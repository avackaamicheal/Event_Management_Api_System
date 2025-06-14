from typing import Optional
from crud.registration import register_crud
from crud.user import user_crud
from crud.event import event_crud
from schemas.registration import Registration, RegistrationBase
from database import registrations


class RegistrationService:
    @staticmethod
    def register_user_service(user_id: int, event_id: int, registration_date:int) -> Registration:
         # Validate user is active
        user = user_crud.get_user_by_id(user_id)
        if not user or not user.is_active:
            raise ValueError("User is not active or doesn't exist")
        
         # Validate event is open
        event = event_crud.get_event_by_id(event_id)
        if not event or not event.is_open:
            raise ValueError("Event is not open for registration")
        
        # Check for existing registration
        existing_reg = next(
            (r for r in registrations
            if r["user_id"] == user_id and r["event_id"] == event_id), 
            None
        )
        if existing_reg:
            raise ValueError("User already registered for this event")
        
        registration_data =  RegistrationBase(user_id = user_id, event_id= event_id, registration_date=registration_date)
    
        return register_crud.register_user(registration_data)

    @staticmethod
    def mark_attendance(registration_id: int) -> Optional[Registration]:
        reg = next((r for r in registrations if r.id == registration_id), None)
        if reg:
            reg.attended = True
            return reg
        return None
    
    @staticmethod
    def get_all_registrations():
        return registrations

    @staticmethod
    def get_user_registrations(user_id: int):
        return [r for r in registrations if r.user_id == user_id]


    

register_service = RegistrationService()