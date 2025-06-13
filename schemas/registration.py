from datetime import date
from pydantic import BaseModel



class RegistrationBase(BaseModel):
    user_id: int
    event_id: int
    registration_date: date

class Registration(RegistrationBase):
    id: int
    attended: bool = False