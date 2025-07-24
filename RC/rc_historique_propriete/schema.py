from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import Schema, fields, validate, validates_schema, ValidationError, EXCLUDE
from .model import RCHistoriquePropriete

class RCHistoriqueProprieteSchema(SQLAlchemySchema):
    class Meta:
        model = RCHistoriquePropriete
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    rc_acteur_id = auto_field(validate=validate.Range(min=1))
    rc_engin_flottant_id = auto_field(validate=validate.Range(min=1))
    date_debut = auto_field(validate=validate.Length(min=1))
    date_fin = auto_field(validate=validate.Length(min=1))
    type_transaction = auto_field(validate=validate.Length(min=1))
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
