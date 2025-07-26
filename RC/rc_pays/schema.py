from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import validate, EXCLUDE
from .model import RCPays

class RCPaysSchema(SQLAlchemySchema):
    class Meta:
        model = RCPays
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    nom = auto_field(validate=validate.Length(min=1))
    code_iso = auto_field(validate=validate.Length(min=1))
    indicatif = auto_field(validate=validate.Length(min=1))
    pavillon_url = auto_field()
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
