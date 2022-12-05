from pydantic import BaseModel

class Appointment_Model(BaseModel):
    tentor_id: str
    course_id: str
    start: str
    end: str

class Change_Appointment_Status(BaseModel):
    id: str
    status: str