from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import Schema, fields, validate, validates_schema, ValidationError, EXCLUDE
from .model import INChecklist

class INChecklistSchema(SQLAlchemySchema):
    class Meta:
        model = INChecklist
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    rc_type_engin_id = auto_field(validate=validate.Range(min=1))
    nom = auto_field(validate=validate.Length(min=1))
    version = auto_field(validate=validate.Length(min=1))
    items = auto_field()
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
