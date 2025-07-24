from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import Schema, fields, validate, validates_schema, ValidationError, EXCLUDE
from .model import AuditLog

class AuditLogSchema(SQLAlchemySchema):
    class Meta:
        model = AuditLog
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    user_id = auto_field(validate=validate.Range(min=1))
    action = auto_field(validate=validate.Length(min=1))
    entite = auto_field(validate=validate.Length(min=1))
    entite_id = auto_field(validate=validate.Range(min=1))
    ancienne_valeur = auto_field()
    nouvelle_valeur = auto_field()
    ip_address = auto_field()
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
