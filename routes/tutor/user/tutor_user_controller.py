from fastapi import APIRouter, Depends

from model.user_model import Update_Tutor_Avail
from service.authentication.auth_bearer import JWTService, JWTBearer
from service.database.database_manager import get_tutor_information_collection, get_user_collection

router = APIRouter(prefix="/information", tags=["Tutor Information"])

@router.get("")
async def get_user_information(user: JWTService = Depends(JWTBearer())):
    tutor_info_collection = get_tutor_information_collection()
    user_collection = get_user_collection()
    info1 = ""
    info2 = ""
    for user_info in tutor_info_collection.find({"_id": user.userId}):
        info1 = user_info
        break
    for user_info in user_collection.find({"_id": user.userId}):
        info2 = user_info["fullname"]
        break
    return {
        "full-name": info2,
        "tutor_info": info1
    }

@router.post("/update")
async def update_user_information(update: Update_Tutor_Avail, user: JWTService = Depends(JWTBearer())):
    if user.access_type < 40:
        return "your are not authorized to go here"
    tutor_info_collection = get_tutor_information_collection()
    tutor_info_collection.update_one({"_id": user.userId},{
        "$set": {
            "from": update.available_from,
            "to": update.untill,
            "komisi": update.komisi
        }
    })
    return {
        "msg": "success"
    }