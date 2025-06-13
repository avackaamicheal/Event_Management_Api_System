from fastapi import FastAPI
from routes.user import user_router
from routes.event import event_router
from routes.registration import registration_router


app= FastAPI(
            
    title= "Event Management API System",
    description="API for managing events, users, speakers, and registrations",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(user_router, prefix="/users", tags= ["Users"])
app.include_router(event_router, prefix="/events", tags= ["Events"])
app.include_router(registration_router,prefix="/registrations", tags=["Registrations"])
