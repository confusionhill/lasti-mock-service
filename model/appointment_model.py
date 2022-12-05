from pydantic import BaseModel

class Appointment_Model(BaseModel):
    tentor_id: str
    course_id: str
    start: str
    end: str