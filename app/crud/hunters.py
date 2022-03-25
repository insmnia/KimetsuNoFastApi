from app.core.config import get_settings, hunters_collection_name
from app.models.hunter import Hunter, HunterInDB
from .mixins import CRUDMixin

settings = get_settings()


class HunterCRUD(CRUDMixin):
    Collection = hunters_collection_name
    CreateScheme = Hunter
    RetrieveScheme = Hunter
    RetrieveDBScheme = HunterInDB
