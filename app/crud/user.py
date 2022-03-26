from app.core.config import users_collection_name
from app.models.user import User, UserInDB
from app.crud.mixins import CRUDMixin


class UserCRUD(CRUDMixin):
    Collection = users_collection_name
    CreateScheme = User
    RetrieveScheme = User
    RetrieveDBScheme = UserInDB
