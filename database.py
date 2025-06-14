from models import User, Event, Speaker, Registration

users: list[User] = [{"id": 1, "name": "Alice", "email": "c@gmail.com", "is_active": True}]
events: list[Event] = []
speakers: list[Speaker] = [
    Speaker(id=1, name="Rotimi Akanni", topic="Full Backend with Python and FastApi"),
    Speaker(id=1, name="Dr. Ada Lovelace", topic="The Future of AI"),
    Speaker(id= 2, name= "Prof. Michael Chen", topic= "Blockchain Fundamentals"),
]

registrations:list[Registration]= [{"user_id": 1, "event_id": 1, "attended": True}]