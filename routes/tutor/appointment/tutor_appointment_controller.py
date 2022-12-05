from fastapi import APIRouter, Depends

from model.appointment_model import Change_Appointment_Status
from service.authentication.auth_bearer import JWTService, JWTBearer
from service.database.database_manager import get_appointment_collection

router = APIRouter(prefix="/appointment", tags=["Appointment"])
@router.get("/incoming")
async def get_incoming_appointment(session: JWTService = Depends(JWTBearer())):
    appointment_collection = get_appointment_collection()
    list_of_appointments = []
    for appointment in appointment_collection.find({
        "tentor_id": session.userId,
        "status": "pending"
    }):
        list_of_appointments.append(appointment)
    return list_of_appointments

@router.get("")
async def get_appointment(session: JWTService = Depends(JWTBearer())):
    appointment_collection = get_appointment_collection()
    data = []
    for appointment in appointment_collection.find({"tentor_id": session.userId}):
        data.append(appointment)
    return data

# update appointment status
@router.post("/status")
async def change_appointment_status(appo: Change_Appointment_Status ,Authorize: JWTService = Depends(JWTBearer())):
    appointment_collection = get_appointment_collection()
    appointment_collection.update_one({"_id": appo.id}, {"$set": {
        "status": appo.status
    }})
    pass