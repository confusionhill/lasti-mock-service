from fastapi import APIRouter, Depends

from service.authentication.auth_bearer import JWTService, JWTBearer

router = APIRouter(prefix="/user", tags=["User"])

@router.get("/courses")
async def get_available_courses(Authorize: JWTService = Depends(JWTBearer())):
    return [
        {}
    ]

@router.get("/courses/{id}")
async def get_course_detail(id:int, Authorize: JWTService = Depends(JWTBearer())):
    return {}

@router.get("/courses/tutor")
async def get_available_tutor():
    return [
        {
            "uid"
            "name": "Rafaela Van Bintang",
            "title" : "Google Android Engineer",
            "komisi": 50000,
            "rating": 4
        }
    ]

@router.post("/appointment")
async def set_appointment(Authorize: JWTService = Depends(JWTBearer())):
    pass

@router.get("/appointment")
async def get_appointment(Authorize: JWTService = Depends(JWTBearer())):
    pass

@router.post("/pay")
async def pay(Authorize: JWTService = Depends(JWTBearer())):
    pass