import uuid

from fastapi import APIRouter, Depends

from model.appointment_model import Appointment_Model
from service.authentication.auth_bearer import JWTService, JWTBearer
from service.database.database_manager import get_tutor_information_collection, get_user_collection, get_appointment_collection

router = APIRouter(prefix="/user", tags=["User"])

@router.get("/courses")
async def get_available_courses(Authorize: JWTService = Depends(JWTBearer())):
    return [
        {}
    ]

@router.get("/courses/{id}")
async def get_course_detail(id:int, Authorize: JWTService = Depends(JWTBearer())):
    return {}

# create an appointment
@router.post("/appointment")
async def set_appointment(appointment: Appointment_Model,Authorize: JWTService = Depends(JWTBearer())):
    appointment_collection = get_appointment_collection()
    appointment_collection.insert_one({
        "_id": uuid.uuid4().hex,
        "tentor_id": appointment.tentor_id,
        "user_id": Authorize.userId,
        "start": appointment.start,
        "end": appointment.end,
        "status": "pending"
    })
    return {
        "msg": "success"
    }

# get list of appointment
@router.get("/appointment")
async def get_appointment(session: JWTService = Depends(JWTBearer())):
    appointment_collection = get_appointment_collection()
    list_of_appointments = []
    for appointment in appointment_collection.find({
        "user_id": session.userId
    }):
        list_of_appointments.append(appointment)
    return list_of_appointments

@router.post("/pay")
async def pay(Authorize: JWTService = Depends(JWTBearer())):
    pass