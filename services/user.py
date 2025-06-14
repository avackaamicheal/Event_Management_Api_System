from database import users, registrations


class UserService():
    @staticmethod
    def get_users_who_attended() -> list:
        attended_user_ids = {r["user_id"] for r in registrations if r["attended"]}
        return [u for u in users if u["id"] in attended_user_ids]


user_service = UserService()