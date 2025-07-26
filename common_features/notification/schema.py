from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import validate, EXCLUDE

from ...constants import NotificationType
from ...utils import flatten_const_values
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
    lu = auto_field()
    type = auto_field(
        validate=[
            validate.Length(min=1),
            validate.OneOf(flatten_const_values(NotificationType))
        ]
    )
    entite_type = auto_field()
    entite_id = auto_field()
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
