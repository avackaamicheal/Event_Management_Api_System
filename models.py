from datetime import date
class User:
    def __init__(
        self, 
        id: int, 
        name: str, 
        email: str, 
        is_active: bool = True
    ):

        self.id = id
        self.name = name
        self.email = email
        self.is_active = is_active

class Event:
    def __init__(
        self,
        id: int,
        title: str,
        location: str,
        date: date, 
        is_open: bool = True
    ):
        self.id = id
        self.title = title
        self.location = location
        self.date = date
        self.is_open = is_open