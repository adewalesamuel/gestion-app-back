from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import Schema, fields, validate, validates_schema, ValidationError, EXCLUDE
from .model import RCPort

class RCPortSchema(SQLAlchemySchema):
    class Meta:
        model = RCPort
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    rc_pays_id = auto_field(validate=validate.Range(min=1))
    nom = auto_field(validate=validate.Length(min=1))
    code = auto_field(validate=validate.Length(min=1))
    capacite_accueil = auto_field(validate=validate.Length(min=1))
    profondeur_max = auto_field(validate=validate.Length(min=1))
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
