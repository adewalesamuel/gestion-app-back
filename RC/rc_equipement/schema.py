from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import validate, EXCLUDE
from .model import RCEquipement

class RCEquipementSchema(SQLAlchemySchema):
    class Meta:
        model = RCEquipement
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    rc_engin_flottant_id = auto_field(validate=validate.Range(min=1))
    nom = auto_field(validate=validate.Length(min=1))
    type = auto_field(validate=validate.Length(min=1))
    numero_serie = auto_field(validate=validate.Length(min=1))
    date_installation = auto_field()
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
