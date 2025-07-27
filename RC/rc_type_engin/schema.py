from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import validate, EXCLUDE

from ...enums import TypeEnginCategorie

from .model import RCTypeEngin

class RCTypeEnginSchema(SQLAlchemySchema):
    class Meta:
        model = RCTypeEngin
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    code = auto_field(validate=validate.Length(min=1))
    libelle = auto_field(validate=validate.Length(min=1))
    categorie = auto_field(validate=validate.OneOf(TypeEnginCategorie))
    tonnage_min = auto_field(validate=validate.Range(min=1))
    tonnage_max = auto_field(validate=validate.Range(min=1))
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
