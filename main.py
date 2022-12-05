from fastapi import FastAPI
import uuid
from model.user_model import User, User_Register
from routes.iot_controller import router as iot_router
from routes.user.user_controller import router as user_router
from routes.tutor.tutor_controller import router as tutor_router
from service.authentication.auth_handler import signJWT, sign_refresh_token
from service.database.database_manager import get_user_collection

app = FastAPI()
app.include_router(user_router)
app.include_router(iot_router)
app.include_router(tutor_router)

@app.post("/login")
async def sign_in_user(user: User):
    user_collection = get_user_collection()
    for user_data in user_collection.find({"username": user.username}):
        if user_data["password"] == user.password:
            return {
                "token": signJWT(user_data["_id"], user_data["type"]),
                 "refresh": sign_refresh_token(user_data["_id"], user.username)
            }
    return "error, user not found"

@app.post("/register")
async def sign_up_user(user: User_Register):
    db = get_user_collection()
    id = uuid.uuid4().hex
    db.insert_one({
        "_id": id ,
        "fullname": user.fullname,
        "username": user.username,
        "password": user.password,
        "type": 1
    })
    return {
        "token": signJWT(id, 1),
        "refresh": sign_refresh_token(id, user.username)
    }

@app.get("/")
async def root():
    return "lorem ipsum dui amet"