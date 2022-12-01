import uuid
from fastapi import FastAPI
from model.user_model import User
from routes.iot_controller import router as iot_router
from routes.user_controller import router as user_router
from routes.tutor_controller import router as tutor_router
from service.authentication.auth_handler import signJWT, sign_refresh_token
from service.database.database_manager import get_user_collection

app = FastAPI()
app.include_router(user_router)
app.include_router(iot_router)
app.include_router(tutor_router)

@app.post("/login")
async def sign_in_user(user: User):
    return {
        "token": signJWT(0, user.username),
        "refresh": sign_refresh_token(0, "user.username")
     }

@app.get("/")
async def root():
    collection_user = get_user_collection()
    for user in collection_user.find({"_id": "U1IT00df001"}):
        return user
    return {"message": "Hello World"}