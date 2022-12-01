from fastapi import APIRouter, Depends
from service.authentication.auth_bearer import JWTService, JWTBearer

router = APIRouter(prefix="/tutor", tags=["Tutor"])

@router.post("/appointment/accept")
async def accept_appointment(Authorize: JWTService = Depends(JWTBearer())):
    pass

@router.get("/appointment")
async def get_appointment(Authorize: JWTService = Depends(JWTBearer())):
    pass