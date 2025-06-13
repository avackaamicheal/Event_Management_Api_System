from typing import List
from fastapi import APIRouter, HTTPException, status
from schemas.registration import RegistrationBase,Registration
from services.registration import register_service

registration_router = APIRouter()

@registration_router.post("/", response_model=Registration, status_code=status.HTTP_201_CREATED)
def register_user(data: RegistrationBase):
    try:
        return register_service.register_user_service(user_id= data.user_id, event_id=data.event_id,  registration_date=data.registration_date )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@registration_router.patch("/{registration_id}/attend", response_model=Registration, status_code= status.HTTP_200_OK)
def mark_attendance(registration_id: int):
    reg = register_service.mark_attendance(registration_id)
    if not reg:
        raise HTTPException(status_code=404, detail="Registration not found")
    return reg

@registration_router.get("/", response_model=List[Registration], status_code= status.HTTP_200_OK)
def get_all_registrations():
    return register_service.get_all_registrations()

@registration_router.get("/user/{user_id}", response_model=List[Registration], status_code= status.HTTP_200_OK)
def get_user_registrations(user_id: int):
    return register_service.get_user_registrations(user_id)