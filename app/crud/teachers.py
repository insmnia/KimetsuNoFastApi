from .mixins import CRUDMixin
from app.models.teacher import Teacher, TeacherInDB
from app.core.config import teachers_collection_name


class TeacherCRUD(CRUDMixin):
    Collection = teachers_collection_name
    CreateScheme = Teacher
    RetrieveScheme = Teacher
    RetrieveDBScheme = TeacherInDB
