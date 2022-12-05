from fastapi import APIRouter
from routes.tutor.appointment.tutor_appointment_controller import router as appointment_router
from routes.tutor.user.tutor_user_controller import router as user_router
from service.database.database_manager import get_user_collection, get_tutor_information_collection

router = APIRouter(prefix="/tutor", tags=["Tutor"])
router.include_router(appointment_router)
router.include_router(user_router)


@router.get("/available")
async def get_available_tutors():
    user_collection = get_user_collection()
    tutor_info_collection = get_tutor_information_collection()
    list_of_tentors = []
    for tentor in user_collection.find({"type" : 40}):
        available = tutor_info_collection.find_one({"_id": tentor["_id"] })
        print(available)
        list_of_tentors.append({
            "id": tentor["_id"],
            "full-name": tentor["fullname"],
            "username": tentor["username"],
            "available-from": available["from"],
            "to": available["to"],
            "komisi": available["komisi"]
        })
    return list_of_tentors
