from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import Schema, fields, validate, validates_schema, ValidationError, EXCLUDE
from .model import EDApi

class EDApiSchema(SQLAlchemySchema):
    class Meta:
        model = EDApi
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    nom = auto_field(validate=validate.Length(min=1))
    description = auto_field()
    url_base = auto_field(validate=validate.Length(min=1))
    statut = auto_field(validate=validate.Length(min=1))
    documentation_url = auto_field(validate=validate.Length(min=1))
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
