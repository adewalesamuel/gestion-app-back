from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import Schema, fields, validate, validates_schema, ValidationError, EXCLUDE
from .model import Role

class RoleSchema(SQLAlchemySchema):
    class Meta:
        model = Role
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    name = auto_field(validate=validate.Length(min=1))
    description = auto_field()
    permissions = auto_field(required=True)
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
