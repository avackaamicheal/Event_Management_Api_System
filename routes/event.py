from fastapi import APIRouter, HTTPException, status
from typing import List
from datetime import date
from schemas.event import Event, EventCreate, EventUpdate
from crud.event import event_crud
from  services.event import event_service as event


event_router = APIRouter()

@event_router.post("/", response_model=Event, status_code=status.HTTP_201_CREATED)
async def create_event(event_data: EventCreate):
    try:
        return event.create_event_service(
            title=event_data.title,
            location=event_data.location,
            date=event_data.date
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    
@event_router.get("/", response_model = List[Event], status_code= status.HTTP_200_OK)
async def get_all_events():
    return event_crud.get_all_events()


@event_router.get("/{event_id}", response_model= Event, status_code= status.HTTP_200_OK)
async def get_event_by_id(event_id: int):
    event_obj = event_crud.get_event_by_id(event_id)
    if not event_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found"
        )
    return event_obj

@event_router.put("/{event_id}", response_model=Event, status_code= status.HTTP_200_OK)
async def update_event(event_id: int, event_data: EventUpdate):
    try:
        updated_event = event.update_event_service(event_id, event_data)
        if not updated_event:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Event not found"
            )
        return updated_event
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    
@event_router.delete("/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_event(event_id: int):
    success = event_crud.delete_event(event_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found"
        )
    return None
    

@event_router.patch("/{event_id}/close", response_model=Event, status_code=status.HTTP_200_OK)
async def close_event_registration(event_id: int):
    closed_event = event.close_event_service(event_id)
    if not closed_event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found"
        )
    return closed_event



