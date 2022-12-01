from pydantic import BaseModel

class feeding_model(BaseModel):
    jam: int
    menit: int

    def toDict(self) -> dict:
        return {
            "jam": self.jam,
            "menit": self.menit
        }

class temperature_model(BaseModel):
    temperature: float