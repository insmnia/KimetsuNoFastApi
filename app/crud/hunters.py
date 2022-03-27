from app.core.config import hunters_collection_name
from app.models.hunter import HunterBase, HunterBaseInDB
from .mixins import CRUDMixin


class HunterCRUD(CRUDMixin):
    Collection = hunters_collection_name
    CreateScheme = HunterBase
    RetrieveScheme = HunterBase
    RetrieveDBScheme = HunterBaseInDB
