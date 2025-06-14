from schemas.user import UserCreate, UserUpdate
from database import users, registrations
from models import User as UserModel

class UserCrud:

    @staticmethod
    def create_user(user_data: UserCreate):
        user_id = len(users) + 1
        user = UserModel(id=user_id, **user_data.model_dump())
        users.append(user)
        return user

    @staticmethod
    def get_user_by_id(user_id: int):
        for user in users:
            if user.id == user_id:
                return user
        return None

    @staticmethod
    def get_all_users():
        return users
    
    @staticmethod
    def update_user(user_id: int, user_data: UserUpdate):
        user = user_crud.get_user_by_id(user_id)
        if user:
            user.name = user_data.name
            user.email = user_data.email
            return user
        return None
    
    @staticmethod
    def delete_user(user_id: int):
        global users
        user = user_crud.get_user_by_id(user_id)
        if not user:
            return False
        # Remove user from the list
        # This is a simple way to remove the user from the list
        users = [user for user in users if user.id != user_id]
        return True
    
    @staticmethod
    def deactivate_user(user_id: int):
        user = user_crud.get_user_by_id(user_id)
        if user:
            user.is_active = not user.is_active
            return user
        return None




user_crud = UserCrud()