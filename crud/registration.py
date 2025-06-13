from database import registrations
from models import Registration as RegistrationModel
from schemas.registration import Registration
from datetime import date


class RegisterCrud:
    @staticmethod
    def register_user(register_data: Registration):

        reg_id = len(registrations) + 1
        registration = Registration(
            id=reg_id,
            user_id=register_data.user_id,
            event_id=register_data.event_id,
            registration_date=register_data.registration_date,
            attended=False
    )
        registrations.append(registration)
        return registration
    

register_crud =RegisterCrud()