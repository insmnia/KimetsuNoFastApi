from typing import List

from pydantic import BaseModel


class Hunter(BaseModel):
    name: str
    style: str
    age: int


class HunterInDB(Hunter):
    id: int


class HunterList(Hunter):
    hunters: List[Hunter]
