from app.crud.mixins import CRUDMixin
from app.models.teacher import TeacherBase, TeacherBaseInDB
from app.core.config import teachers_collection_name


class TeacherCRUD(CRUDMixin):
    Collection = teachers_collection_name
    CreateScheme = TeacherBase
    RetrieveScheme = TeacherBase
    RetrieveDBScheme = TeacherBaseInDB
