from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import Schema, fields, validate, validates_schema, ValidationError, EXCLUDE
from .model import Notification

class NotificationSchema(SQLAlchemySchema):
    class Meta:
        model = Notification
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    user_id = auto_field(validate=validate.Range(min=1))
    titre = auto_field(validate=validate.Length(min=1))
    message = auto_field(validate=validate.Length(min=1))
    lu = auto_field(validate=validate.Length(min=1))
    type = auto_field(validate=validate.Length(min=1))
    entite_type = auto_field(validate=validate.Length(min=1))
    entite_id = auto_field(validate=validate.Range(min=1))
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
