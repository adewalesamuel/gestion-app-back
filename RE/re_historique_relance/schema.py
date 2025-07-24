from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import Schema, fields, validate, validates_schema, ValidationError, EXCLUDE
from .model import REHistoriqueRelance

class REHistoriqueRelanceSchema(SQLAlchemySchema):
    class Meta:
        model = REHistoriqueRelance
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    re_relance_id = auto_field(validate=validate.Range(min=1))
    user_id = auto_field(validate=validate.Range(min=1))
    date = auto_field()
    heure = auto_field()
    mode = auto_field(validate=validate.Length(min=1))
    contenu = auto_field(validate=validate.Length(min=1))
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
