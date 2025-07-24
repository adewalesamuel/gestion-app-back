from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import Schema, fields, validate, validates_schema, ValidationError, EXCLUDE
from .model import RETarif

class RETarifSchema(SQLAlchemySchema):
    class Meta:
        model = RETarif
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    service = auto_field(validate=validate.Length(min=1))
    montant = auto_field(validate=validate.Length(min=1))
    devise = auto_field(validate=validate.Length(min=1))
    frequence = auto_field(validate=validate.Length(min=1))
    type_acteur = auto_field(validate=validate.Length(min=1))
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
