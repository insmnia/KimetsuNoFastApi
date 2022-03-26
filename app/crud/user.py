from app.core.config import users_collection_name
from app.models.user import UserBase, UserInDB, UserCreate
from app.crud.mixins import CRUDMixin


class UserCRUD(CRUDMixin):
    Collection = users_collection_name
    CreateScheme = UserCreate
    RetrieveScheme = UserBase
    RetrieveDBScheme = UserInDB
