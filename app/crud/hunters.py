from app.core.config import hunters_collection_name
from app.models.hunter import Hunter, HunterInDB
from .mixins import CRUDMixin


class HunterCRUD(CRUDMixin):
    Collection = hunters_collection_name
    CreateScheme = Hunter
    RetrieveScheme = Hunter
    RetrieveDBScheme = HunterInDB
