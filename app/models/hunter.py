from pydantic import BaseModel, Field
from app.core.utils import OID, MongoModel


class Hunter(BaseModel):
    name: str
    style: str
    age: int


class HunterInDB(MongoModel, Hunter):
    id: OID = Field(alias="_id")
