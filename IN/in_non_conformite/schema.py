from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import Schema, fields, validate, validates_schema, ValidationError, EXCLUDE
from .model import INNonConformite

class INNonConformiteSchema(SQLAlchemySchema):
    class Meta:
        model = INNonConformite
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    in_inspection_id = auto_field(validate=validate.Range(min=1))
    user_id = auto_field(validate=validate.Range(min=1))
    description = auto_field()
    gravite = auto_field(validate=validate.Length(min=1))
    date_decouverte = auto_field(validate=validate.Length(min=1))
    heure = auto_field()
    date_resolution = auto_field(validate=validate.Length(min=1))
    statut = auto_field(validate=validate.Length(min=1))
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
