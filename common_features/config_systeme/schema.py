from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import Schema, fields, validate, validates_schema, ValidationError, EXCLUDE
from .model import ConfigSysteme

class ConfigSystemeSchema(SQLAlchemySchema):
    class Meta:
        model = ConfigSysteme
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    parametre = auto_field(validate=validate.Length(min=1))
    valeur = auto_field(validate=validate.Length(min=1))
    module = auto_field(validate=validate.Length(min=1))
    editable = auto_field(validate=validate.OneOf([True, False]))
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
