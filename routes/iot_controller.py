from fastapi import APIRouter, Depends
import datetime
from model.iot_model import feeding_model, temperature_model
from service.database.database_manager import get_temperature_collection, get_feed_collection

router = APIRouter(prefix="/iot", tags=["IOT"])

@router.post("/temperature/")
async def update_temperature(value: temperature_model):
    db = get_temperature_collection()
    try:
        db.update_one(
            {"_id": 1},
            {"$set": {"temperature": value.temperature}}
        )
        return {
            "msg": "success"
        }
    except:
        return {"msg": "error"}

@router.get("/temperature")
async def get_temperature():
    db = get_temperature_collection()
    try:
        find = db.find_one({"_id": 1})
        return {
            "msg": "success",
            "temperature": find["temperature"],
            "in": "celcius"
        }
    except:
        return {"msg": "error"}

@router.post("/feeding")
async def add_feeding_time(time: feeding_model):
    db = get_feed_collection()
    db.insert_one(time.toDict())
    return {
        "msg": "success"
    }

@router.get("/feeding")
async def get_feeding_time() -> bool:
    db = get_feed_collection()
    now = datetime.datetime.now()
    find = db.find_one({
        "jam": now.hour,
        "menit": now.minute
    })
    return find != None