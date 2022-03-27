from pydantic import BaseModel, Field
from app.core.utils import OID, MongoModel


class TeacherBase(BaseModel):
    name: str
    style: str


class TeacherBaseInDB(MongoModel, TeacherBase):
    id: OID = Field(alias="_id")
