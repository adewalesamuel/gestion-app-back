from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import Schema, fields, validate, validates_schema, ValidationError, EXCLUDE
from .model import GUHistorique

class GUHistoriqueSchema(SQLAlchemySchema):
    class Meta:
        model = GUHistorique
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    user_id = auto_field(validate=validate.Range(min=1))
    gu_demande_id = auto_field(validate=validate.Range(min=1))
    action = auto_field(validate=validate.Length(min=1))
    details = auto_field(validate=validate.Length(min=1))
    date = auto_field()
    heure = auto_field()
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
