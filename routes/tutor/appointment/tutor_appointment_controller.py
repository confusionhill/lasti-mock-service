from fastapi import APIRouter, Depends
from service.authentication.auth_bearer import JWTService, JWTBearer
from service.database.database_manager import get_appointment_collection

router = APIRouter(prefix="/appointment", tags=["Appointment"])
@router.get("/incoming")
async def accept_appointment(session: JWTService = Depends(JWTBearer())):
    appointment_collection = get_appointment_collection()
    list_of_appointments = []
    for appointment in appointment_collection.find({
        "tentor_id": session.userId
    }):
        list_of_appointments.append(appointment)
    return list_of_appointments

@router.get("")
async def get_appointment(Authorize: JWTService = Depends(JWTBearer())):
    pass

# update appointment status
@router.post("/status")
async def change_appointment_status(Authorize: JWTService = Depends(JWTBearer())):
    pass