from fastapi import FastAPI
from routes.user import user_router


app= FastAPI(title= "Event Management API System")

app.include_router(user_router, prefix="/users", tags= ["users"])
