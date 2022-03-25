from pydantic import BaseModel, Field
from app.core.utils import OID, MongoModel


class Teacher(BaseModel):
    name: str
    style: str


class TeacherInDB(MongoModel, Teacher):
    id: OID = Field(alias="_id")
