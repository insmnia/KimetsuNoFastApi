from pydantic import BaseModel, Field
from app.core.utils import OID, MongoModel


class HunterBase(BaseModel):
    name: str
    style: str
    age: int


class HunterBaseInDB(MongoModel, HunterBase):
    id: OID = Field(alias="_id")
