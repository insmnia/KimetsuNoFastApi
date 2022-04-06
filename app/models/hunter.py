from pydantic import BaseModel, Field
from app.core.utils import OID, MongoModel
from app.models.teacher import TeacherBaseInDB


class HunterBase(BaseModel):
    name: str
    style: str
    age: int


class HunterBaseInDB(MongoModel, HunterBase):
    id: OID = Field(alias="_id")


class HunterFull(HunterBaseInDB):
    teacher: TeacherBaseInDB = None
